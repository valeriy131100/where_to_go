# Generated by Django 3.2.12 on 2022-02-07 08:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20220204_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(verbose_name='полное описание'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='position',
            field=models.IntegerField(default=0, verbose_name='позиция'),
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together={('longitude', 'latitude')},
        ),
    ]
