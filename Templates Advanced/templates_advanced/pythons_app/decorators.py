from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_groups(allowed=[]):
    def decorator(view_func):
        def wrapper(req, *args, **kwargs):
            if req.user.groups.exists():
                for group in req.user.groups.all():
                    if group.name in allowed:
                        return view_func(req, *args, **kwargs)
            else:
                return redirect('page 401')
                # return HttpResponse('401 Unauthorized!')
        return wrapper
    return decorator