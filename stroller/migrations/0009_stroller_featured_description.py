# Generated by Django 5.0.7 on 2024-07-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stroller', '0008_stroller_featured_photo_stroller_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='stroller',
            name='featured_description',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
