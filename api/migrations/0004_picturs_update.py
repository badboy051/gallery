# Generated by Django 2.2.3 on 2020-05-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200502_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturs',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]