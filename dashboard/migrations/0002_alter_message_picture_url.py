# Generated by Django 4.1 on 2022-08-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='picture_url',
            field=models.CharField(blank=True, default=None, max_length=1024, null=True),
        ),
    ]