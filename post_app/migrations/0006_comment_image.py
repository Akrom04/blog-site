# Generated by Django 4.2.5 on 2023-12-31 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0005_remove_comment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.FileField(default='comment-image/user.jpg', upload_to='comment-image'),
        ),
    ]
