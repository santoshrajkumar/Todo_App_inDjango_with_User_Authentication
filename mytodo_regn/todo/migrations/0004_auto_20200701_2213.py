# Generated by Django 3.0.3 on 2020-07-01 16:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0003_customertodoitems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerToDoItems',
            new_name='CustomerToDoItem',
        ),
    ]
