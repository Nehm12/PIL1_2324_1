from django.contrib import admin
from .models import Profile, Interest, ProfileInterests


# Register your models here.

admin.site.register(Profile)
admin.site.register(Interest)
admin.site.register(ProfileInterests)