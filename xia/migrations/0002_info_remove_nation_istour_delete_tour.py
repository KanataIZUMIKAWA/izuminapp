# Generated by Django 4.0 on 2022-10-06 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raid', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='nation',
            name='istour',
        ),
        migrations.DeleteModel(
            name='Tour',
        ),
    ]