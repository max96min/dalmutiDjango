# Generated by Django 3.1.1 on 2020-09-21 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dalmuti', '0008_gamer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamer',
            name='taxYn',
            field=models.BooleanField(default=False),
        ),
    ]
