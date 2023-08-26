from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models



@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "price", "id"]


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.CartProduct, admin.ModelAdmin)
admin.site.register(models.Cart, admin.ModelAdmin)