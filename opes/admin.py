from django.contrib import admin
from .models import Client

class MemberAdmin(admin.ModelAdmin):
      list_display    = ['firstname', 'lastname', 'email', 'phone', 'message']
      
admin.site.register(Client, MemberAdmin)
