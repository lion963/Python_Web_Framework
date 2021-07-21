from django.template import Library

from Textile_Market.textile_profile.models import Profile

register = Library()


@register.inclusion_tag('tags/profile_complete_notification.html', takes_context=True)
def profile_complete_notification(context):
    if context.request.user.id:
        user_id = context.request.user.id
        profile = Profile.objects.get(pk=user_id)
        complete = all([profile.first_name, profile.last_name, profile.type, profile.telephone, profile.image])
        if not complete:
            return {'is_complete': False}
        return {'is_complete': True}
    else:
        return {'is_complete': True}
