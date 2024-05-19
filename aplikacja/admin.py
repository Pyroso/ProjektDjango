from django.contrib import admin
from .models import Notatka


# admin.site.register(Notatka)
@admin.register(Notatka)
class NotatkaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
# Register your models here.
