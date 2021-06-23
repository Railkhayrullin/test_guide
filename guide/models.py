from django.db import models
import datetime


class Guide(models.Model):
    """Справочник"""
    name = models.CharField('наименование', max_length=255, db_index=True)
    short_name = models.CharField('короткое наименование', max_length=128)
    description = models.TextField('описание')
    version = models.CharField('версия', max_length=64, unique=True)
    date = models.DateField('дата начала действия справочника этой версии', default=datetime.date.today)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'справочник'
        verbose_name_plural = 'справочники'


class GuideElement(models.Model):
    """Элемент справочника"""
    guide = models.ForeignKey(Guide,
                              on_delete=models.CASCADE,
                              related_name='guide_elements',
                              verbose_name='родительский идентификатор',
                              null=True,
                              db_index=True)
    element_code = models.CharField('код элемента', max_length=64, blank=False)
    element_value = models.CharField('значение элемента', max_length=255, blank=False)

    def __str__(self):
        return self.element_value

    class Meta:
        verbose_name = 'элемент справочника'
        verbose_name_plural = 'элементы справочника'
