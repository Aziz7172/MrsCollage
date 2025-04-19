from django.contrib import admin
from django.utils.html import format_html
from .models import Paint

@admin.register(Paint)
class PaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image', 'description_short')
    
    def display_image(self, obj):
        if obj.image:  # تأكد من وجود صورة
            return format_html(
                '<img src="{}" style="height: 50px; border-radius: 4px;" />', 
                obj.image.url
            )
        return "No Image"
    display_image.short_description = 'Image'  # عنوان العمود
    
    def description_short(self, obj):
        return obj.description[:50] + '...' if obj.description else "No Description"
    description_short.short_description = 'Description'


    # يمكنك إضافة هذا داخل الكلاس إذا أردت زر معاينة كامل
    readonly_fields = ('image_preview',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px;" />',
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = 'Preview'