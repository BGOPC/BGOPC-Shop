# Generated by Django 4.0.6 on 2022-07-11 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messages',
            new_name='adminresponse',
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]