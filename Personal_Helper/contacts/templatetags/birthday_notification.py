
from django import template
from django.db.models import Count, F
from contacts.models import *


from django.db.models.functions import ExtractMinute
register = template.Library()


@register.inclusion_tag('contacts/birthday_notification_template.html', takes_context=True)
def show_birthday(context):
    # categories = Category.objects.all()
    # news = News.objects.order_by('-create_at').distinct('category_id')
    # print(news)
    # categories = cache.get('categories')
    # if not categories:
    #     categories = Category.objects.annotate(cnt=Count('news'), filter=F('news__is_published')).filter(
    #         cnt__gt=0).order_by('-update_at_last_news')
    #     cache.set('categories', categories, 30)
    birthday_contact = Contacts.objects.filter(user_id=context['request'].user.id)
    data = []
    for contact in birthday_contact:
        if contact.days_to_birthday() < 8:
            data.append(contact)
    return {'birthdays': data}
