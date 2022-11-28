# Generated by Django 4.0 on 2022-11-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subeana', '0008_remove_ai_bad_remove_ai_good_ai_isbad_ai_isgood'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ai',
            old_name='isbad',
            new_name='isgpt',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='isgood',
        ),
        migrations.AddField(
            model_name='ai',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
