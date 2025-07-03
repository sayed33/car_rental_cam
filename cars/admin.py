from django.contrib import admin
from django.utils.html import format_html
from .models import Car, CarImage


admin.site.site_header = "CarCam لوحة التحكم"
admin.site.site_title = "CarCam"
admin.site.index_title = "مرحبا بك في لوحة التحكم"

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1  # عدد الصور الجديدة الجاهزة للإضافة

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_type', 'car_number', 'created_at', 'first_image')
    search_fields = ('car_type', 'car_number')
    list_filter = ('car_type', 'created_at')
    inlines = [CarImageInline]

    def first_image(self, obj):
        image = obj.images.first()  # related_name='images'
        if image:
            return format_html('<img src="{}" width="100" height="60" style="object-fit:cover;" />', image.image.url)
        return "-"
    first_image.short_description = 'صورة السيارة'
    first_image.allow_tags = True


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('car', 'timestamp')
