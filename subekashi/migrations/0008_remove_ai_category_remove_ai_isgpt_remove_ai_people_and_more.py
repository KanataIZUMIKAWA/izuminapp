# Generated by Django 4.0 on 2022-12-08 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subekashi', '0007_alter_song_imitate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ai',
            name='category',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='isgpt',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='people',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='similar',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='title',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='users',
        ),
        migrations.CreateModel(
            name='Genesong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('similar', models.CharField(default='', max_length=100)),
                ('ai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subekashi.ai')),
            ],
        ),
        migrations.CreateModel(
            name='Genecategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=100)),
                ('ai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subekashi.ai')),
            ],
        ),
    ]