from django.shortcuts import redirect


def allowed_groups(allowed=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            if request.user.groups.exists():
                for group in request.user.groups.all():
                    if group.name in allowed:
                        return view_func(request, *args, **kwargs)
                    else:
                        return redirect('page 401')
            else:
                return redirect('page 401')
        return wrapper
    return decorator