from django.http import HttpResponse
from django.shortcuts import redirect
from apps.useraccount.models import Profile


# just manager can see
def FandB_user(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.profile.IndustrySel_id == 2 or request.user.is_superuser:
            return views_func(request, *args, **kwargs)
        else:
            return redirect('dashboard:panel')

    return wrapper_func
