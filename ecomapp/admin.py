from django.contrib import admin
from .models import customerrole
# Register your models here.
@admin.register(customerrole)
class customerroleAdmin(admin.ModelAdmin):
    list_display= ("id", "Group_Name","Group_Level","Status", "Image" )