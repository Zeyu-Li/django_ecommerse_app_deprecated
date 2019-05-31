from django.contrib import admin
from login.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')

    def user_info(self, obj):
        return obj.email

admin.site.register(UserProfile, UserProfileAdmin)
