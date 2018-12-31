from django.contrib import admin
from .models import MailingList, Subscriber, Message


admin.site.register(MailingList)
admin.site.register(Subscriber)
admin.site.register(Message)
