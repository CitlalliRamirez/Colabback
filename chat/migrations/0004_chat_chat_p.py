# Generated by Django 3.2.6 on 2021-09-06 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_chat_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chat_p',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
