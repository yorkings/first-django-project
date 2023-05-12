from django.contrib import admin
from practice.models import Member 
# Register your models here.
class AdminCon(admin.ModelAdmin):
    list_display = ('name','last','email')
admin.site.register(Member,AdminCon)
