from django.contrib import admin
from .models import Blog, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug") # liste görünümü
    list_editable = ("is_active","is_home",) # listede edit yapılabilir
    search_fields = ("title","description",) # serach bar
    readonly_fields = ("slug",) # sadece okunabilir


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)