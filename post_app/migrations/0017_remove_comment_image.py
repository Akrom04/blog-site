# Generated by Django 4.2.5 on 2024-01-01 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0016_alter_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
    ]