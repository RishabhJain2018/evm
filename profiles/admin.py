from django.contrib import admin
from .models import UserDetail


class UserAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'github', 'linkedin', 'contact_no')


admin.site.register(UserDetail, UserAdmin)
