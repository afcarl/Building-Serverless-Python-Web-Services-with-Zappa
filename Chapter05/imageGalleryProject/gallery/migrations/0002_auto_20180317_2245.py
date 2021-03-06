# Generated by Django 2.0.3 on 2018-03-17 22:45

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default='100', editable=False, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, default='100', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(height_field='image_height', upload_to=gallery.models.upload_path, verbose_name='image', width_field='image_width'),
        ),
    ]
