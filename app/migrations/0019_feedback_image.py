# Generated by Django 5.1.4 on 2025-05-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='feedback_images/'),
        ),
    ]
