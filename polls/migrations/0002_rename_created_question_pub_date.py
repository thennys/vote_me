# Generated by Django 5.1.4 on 2025-01-02 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='created',
            new_name='pub_date',
        ),
    ]
