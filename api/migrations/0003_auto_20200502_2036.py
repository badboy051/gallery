# Generated by Django 3.0.5 on 2020-05-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200502_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturs',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='picturs',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]