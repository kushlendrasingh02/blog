# Generated by Django 4.2.2 on 2023-06-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click on the title to read the full article...', max_length=255),
        ),
    ]