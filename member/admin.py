from django.contrib import admin

# Register your models here.
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'created_at', 'updated_at')

admin.site.register(Member, MemberAdmin)