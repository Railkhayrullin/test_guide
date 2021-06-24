# Generated by Django 3.2.4 on 2021-06-24 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guideelement',
            options={'verbose_name': 'элемент справочника', 'verbose_name_plural': 'элементы справочника'},
        ),
        migrations.AlterField(
            model_name='guide',
            name='short_name',
            field=models.SlugField(max_length=64, verbose_name='короткое наименование'),
        ),
    ]
