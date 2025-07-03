from django.contrib import admin
from .models import Car

class MyAdminSite(admin.AdminSite):
    site_header = "Car Camera Dashboard"
    site_title = "CarCam Admin"
    index_title = "Welcome to CarCam Admin Panel"

admin_site = MyAdminSite(name='myadmin')

@admin.register(Car, site=admin_site)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_type', 'car_number', 'timestamp')
    search_fields = ('car_type', 'car_number')
    list_filter = ('timestamp',)

# تحميل ملف CSS
admin.site.site_header = "Car Camera Dashboard"
admin.site.site_title = "CarCam Admin"
admin.site.index_title = "Welcome to CarCam Admin Panel"

class CustomAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ['camera/admin.css']
        }

# لو أردت تطبيق الـ CSS على كل النماذج، أضف CustomAdmin بدلًا من admin.ModelAdmin
