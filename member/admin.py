from django.contrib import admin

# Register your models here.
from .models import Member

class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'created_at', 'updated_at')

admin.site.register(Member, BoardMemberAdmin)