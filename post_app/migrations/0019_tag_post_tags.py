# Generated by Django 4.2.5 on 2024-01-02 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0018_comment_image_comment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='post_app.tag'),
        ),
    ]