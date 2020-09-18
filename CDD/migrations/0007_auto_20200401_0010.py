
# Generated by Django 3.0.3 on 2020-03-31 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CDD', '0006_auto_20200331_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claims',
            old_name='cost_estimation',
            new_name='total_cost_estimation',
        ),
        migrations.RenameField(
            model_name='partcost',
            old_name='light',
            new_name='boot',
        ),
        migrations.RemoveField(
            model_name='partcost',
            name='roof',
        ),
        migrations.RemoveField(
            model_name='partcost',
            name='sideglass',
        ),
        migrations.AddField(
            model_name='claims',
            name='bool_boot',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='claims',
            name='bool_bumper_front',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='claims',
            name='bool_bumper_rear',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='claims',
            name='bool_door_left',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='claims',
            name='bool_door_right',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='claims',
            name='bool_hood',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='claims',
            name='bool_is_car',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='claims',
            name='bool_window_left',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='claims',
            name='bool_window_right',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='claims',
            name='bool_windshield_front',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='claims',
            name='bool_windshield_rear',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='degree',
            field=models.CharField(max_length=32),
        ),
    ]
