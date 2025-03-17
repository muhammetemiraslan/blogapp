from django.contrib import admin
from .models import Blog, Category
from django.utils.safestring import mark_safe

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug","selected_categories") # liste görünümü / 
    list_editable = ("is_active","is_home",) # listede edit yapılabilir
    search_fields = ("title","description",) # serach bar
    readonly_fields = ("slug",) # sadece okunabilir
    list_filter = ("is_active","is_home","categories",)

    def selected_categories(self, obj): # methoda parametre olarak gider
        html = ""

        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"
        html +=  "</ul>"
        return mark_safe(html)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)