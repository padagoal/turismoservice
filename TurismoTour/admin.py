from django.contrib import admin
from .models import Tour
# Register your models here.


class TourAdmin(admin.ModelAdmin):
    list_display = (('tour_name'),('is_from_user'),('is_from_staff'),)
    search_fields = (('tour_name'),)



admin.site.register(Tour,TourAdmin)