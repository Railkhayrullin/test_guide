from django.contrib import admin

from guide.models import Guide, GuideElement


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    """Справочник"""
    list_display = ('name', 'id', 'version', 'date')
    list_display_links = ('name',)
    search_fields = ('name', 'id', 'version', 'date')
    list_filter = ('date',)


@admin.register(GuideElement)
class GuideElementAdmin(admin.ModelAdmin):
    """Элемент справочника"""
    list_display = ('element_code', 'id', 'guide')
    list_display_links = ('element_code',)
    search_fields = ('element_code', 'id', 'guide')
    list_filter = ('element_code', 'id', 'guide')


admin.site.site_title = 'для ООО «КОМТЕК»'
admin.site.site_header = 'Тестовое задание для ООО «КОМТЕК»'
