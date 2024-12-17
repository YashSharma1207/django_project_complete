from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from .ctl.RegistrationCtl import RegistrationCtl
from .ctl.LoginCtl import LoginCtl

from .ctl.WelcomeCtl import WelcomeCtl


# from .ctl.UserCtl import UserCtl
# from .ctl.UserListCtl import UserListCtl
# from .ctl.RoleCtl import RoleCtl
# from .ctl.RoleListCtl import RoleListCtl


@csrf_exempt
def action(request, page):
    ctlName = page + "Ctl()"
    ctlObj = eval(ctlName)
    return ctlObj.execute(request, {"id": 0})


def index(request):
    res = render(request, 'Welcome.html')
    return res


def auth():
    return None
