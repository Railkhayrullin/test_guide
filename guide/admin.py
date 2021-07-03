from django.contrib import admin

from guide.models import Guide, GuideElement


class GuideElementInline(admin.TabularInline):
    """Элемент справочника"""
    model = GuideElement
    extra = 0


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    """Справочник"""
    list_display = ('name', 'version', 'date', 'id')
    list_display_links = ('name',)
    search_fields = ('name', 'id', 'version', 'date')
    list_filter = ('date',)
    inlines = [GuideElementInline, ]
    ordering = ('name', '-version')


admin.site.site_title = 'для ООО «КОМТЕК»'
admin.site.site_header = 'Тестовое задание для ООО «КОМТЕК»'
