# Generated by Django 4.0.2 on 2022-08-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xia', '0006_alter_nation_king'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='nation',
            field=models.CharField(default='', max_length=50),
        ),
    ]
