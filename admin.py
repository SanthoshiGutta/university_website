from django.contrib import admin
from .models import Admin
from .forms import AdminForm

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    form = AdminForm   # attach the custom form
    list_display = ('name', 'father_name', 'gender', 'hall_ticket_number', 'branch', 'college')

