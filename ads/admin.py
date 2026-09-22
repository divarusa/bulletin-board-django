from django.contrib import admin

# Register your models here.

from .models import Ad, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "category", "author", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title", "description")
