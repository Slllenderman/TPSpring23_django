# Generated by Django 4.2 on 2023-04-20 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askPupkin_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-creation_date']},
        ),
    ]
