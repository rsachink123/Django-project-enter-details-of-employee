from django.contrib import admin
from genericviews.models import Person
class AdminPerson(admin.ModelAdmin):
    list_display = ['name','company_name','location','email','mobile','desc']
admin.site.register(Person,AdminPerson)
