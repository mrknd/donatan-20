# Generated by Django 3.2 on 2024-08-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stroller', '0009_stroller_featured_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='stroller',
            name='description_first',
            field=models.TextField(blank=True, null=True, verbose_name='Перший опис'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='description_fourth',
            field=models.TextField(blank=True, null=True, verbose_name='Четвертий опис'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='description_second',
            field=models.TextField(blank=True, null=True, verbose_name='Другий опис'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='description_third',
            field=models.TextField(blank=True, null=True, verbose_name='Третій опис'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='header_first',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Перший заголовок опису'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='header_fourth',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Четвертий заголовок опису'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='header_second',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Другий заголовок опису'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='header_third',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Третій заголовок опису'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='photo_first',
            field=models.ImageField(blank=True, null=True, upload_to='stroller_photo', verbose_name='Перше фото опису'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='photo_fourth',
            field=models.ImageField(blank=True, null=True, upload_to='stroller_photo', verbose_name='Четверте фото опису'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='photo_second',
            field=models.ImageField(blank=True, null=True, upload_to='stroller_photo', verbose_name='Друге фото опису'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='photo_third',
            field=models.ImageField(blank=True, null=True, upload_to='stroller_photo', verbose_name='Третє фото опису'),
        ),
        migrations.AddField(
            model_name='stroller',
            name='sized_stroller',
            field=models.ImageField(blank=True, null=True, upload_to='stroller_photo', verbose_name='Фото коляски з розмірами'),
        ),
    ]
