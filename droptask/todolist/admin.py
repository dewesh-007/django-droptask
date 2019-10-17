from django.contrib import admin
from todolist.models import Tasklist, UserProfileInfo

# Register your models here.
admin.site.register(Tasklist)
admin.site.register(UserProfileInfo)
