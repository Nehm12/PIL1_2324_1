from django.contrib import admin
from chat.models import Message, list_user
# Register your models here.

admin.site.register(Message)
admin.site.register(list_user)
