from django.shortcuts import redirect


class GroupRequiredMixin:
    required_groups = ['Company']

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        if not request.user.is_authenticated:
            return redirect('page 401')

        if not request.user.groups.exists():
            return redirect('page 401')

        user_group_names = [g.name for g in request.user.groups.all()]
        result = set(user_group_names).intersection(self.required_groups)
        if self.required_groups and not result:
            return redirect('page 401')

        return super().dispatch(request, *args, **kwargs)