# Generated by Django 5.0.3 on 2024-03-20 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_remove_contact_category_contact_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='categoria',
            new_name='category',
        ),
    ]
