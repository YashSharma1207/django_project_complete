from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .ctl.RegistrationCtl import RegistrationCtl
from .ctl.LoginCtl import LoginCtl
from .ctl.WelcomeCtl import WelcomeCtl
from .ctl.UserCtl import UserCtl
from .ctl.RoleCtl import RoleCtl
from .ctl.UserListCtl import UserListCtl
from .ctl.ForgetPasswordCtl import ForgetPasswordCtl
from .ctl.AttributeCtl import AttributeCtl
from .ctl.AttributeListCtl import AttributeListCtl
from .ctl.InitiativeCtl import InitiativeCtl
from .ctl.InitiativeListCtl import InitiativeListCtl
from .ctl.EmployeeCtl import EmployeeCtl
from .ctl.EmployeeListCtl import EmployeeListCtl

@csrf_exempt
def action(request, page="", operation="", id=0):
    if page == "Logout":
        Session.objects.all().delete()
        request.session['user'] = None
        page = "Login"
    ctlName = page + "Ctl()"
    ctlObj = eval(ctlName)
    res = ctlObj.execute(request, {"operation": operation, "id": id})
    return res


def index(request):
    res = render(request, 'Welcome.html')
    return res
