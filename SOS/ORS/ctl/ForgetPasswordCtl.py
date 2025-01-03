from .BaseCtl import BaseCtl
from django.shortcuts import render, redirect
from ..utility.DataValidator import DataValidator
from ..service.ForgetPasswordService import ForgetPasswordService
from ..service.EmailService import EmailService
from ..service.EmailMessege import EmailMessege
from ..models import User


class ForgetPasswordCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['loginId'] = requestForm['loginId']

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if DataValidator.isNull(self.form['loginId']):
            inputError['loginId'] = "Login ID Can Not Be Null"
            self.form['error'] = True
        else:
            if (DataValidator.isEmail(self.form['loginId'])):
                inputError['loginId'] = "Login ID Must Be Like example@gmail.com"
                self.form['error'] = True
        return self.form['error']

    def display(self, request, params={}):
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        try:
            user = User.objects.get(loginId=self.form['loginId'])

            emailMessege = EmailMessege()
            emailMessege.to = [user.loginId]
            emailMessege.subject = "Forget Password"

            mail_response = EmailService.send(emailMessege, "forgotPassword", user)

            if mail_response == 1:
                self.form['error'] = False
                self.form['message'] = "Your Password Has Been Sent Successfully"
                request.session['user'] = user.firstName
            else:
                self.form['error'] = True
                self.form['message'] = "Please Check Your Internet Connection"

        except User.DoesNotExist:
            self.form['error'] = True
            self.form['message'] = "Login ID is Incorrect"
        except Exception as e:
            self.form['error'] = True
            self.form['message'] = f"An unexpected error occurred: {str(e)}"

        return render(request, self.get_template(), {'form': self.form})


    def get_template(self):
        return "ForgetPassword.html"

    def get_service(self):
        return ForgetPasswordService()
