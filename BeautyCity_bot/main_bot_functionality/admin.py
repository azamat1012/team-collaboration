from django.contrib import admin
from .models import Specialist, Appointment, Payment, Notification, SalonManager


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['name', 'biography', 'specialization', 'availability']


admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(Notification)
admin.site.register(SalonManager)
