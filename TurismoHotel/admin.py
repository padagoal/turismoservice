from django.contrib import admin
from TurismoHotel.models import *
# Register your models here.


admin.site.register(ServiceHotel)
admin.site.register(ServiceRoom)


admin.site.register(Hotel)
admin.site.register(Rooms)

admin.site.register(PhotosRoom)