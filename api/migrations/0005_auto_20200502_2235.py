# Generated by Django 2.2.3 on 2020-05-02 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_picturs_update'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='picturs',
            new_name='Pictures',
        ),
        migrations.AlterField(
            model_name='pictures',
            name='album_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Albums'),
        ),
        migrations.AlterUniqueTogether(
            name='albums',
            unique_together={('author', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='pictures',
            unique_together={('title', 'album_id')},
        ),
    ]
