# Generated by Django 4.0.2 on 2022-04-26 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('izuminapp', '0005_firstview_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iscitizen', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('nickname', models.CharField(default='', max_length=50)),
                ('population', models.IntegerField(default=0)),
                ('area', models.IntegerField(default=0)),
                ('x', models.IntegerField(default=0)),
                ('z', models.IntegerField(default=0)),
                ('info', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='firstview',
            name='player',
        ),
        migrations.RemoveField(
            model_name='player',
            name='crime',
        ),
        migrations.RemoveField(
            model_name='player',
            name='leave',
        ),
        migrations.RemoveField(
            model_name='player',
            name='primary',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rank',
        ),
        migrations.AddField(
            model_name='player',
            name='goldsam',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='firstview',
            name='title',
            field=models.CharField(default='無題', max_length=20),
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('nickname', models.CharField(default='', max_length=50)),
                ('population', models.IntegerField(default=0)),
                ('area', models.IntegerField(default=0)),
                ('x', models.IntegerField(default=0)),
                ('z', models.IntegerField(default=0)),
                ('info', models.CharField(default='', max_length=200)),
                ('mayor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='town_mayor', to='izuminapp.player')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(default='', max_length=500)),
                ('nation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='izuminapp.nation')),
            ],
        ),
        migrations.AddField(
            model_name='nation',
            name='capital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='izuminapp.town'),
        ),
        migrations.AddField(
            model_name='nation',
            name='king',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='nation_king', to='izuminapp.player'),
        ),
        migrations.CreateModel(
            name='Minister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='大臣', max_length=20)),
                ('isminister', models.BooleanField(default=True)),
                ('citizen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='izuminapp.citizen')),
            ],
        ),
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='izuminapp.player')),
            ],
        ),
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(default='', max_length=20)),
                ('x', models.IntegerField(default=0)),
                ('z', models.IntegerField(default=0)),
                ('isunderground', models.BooleanField(default=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='izuminapp.player')),
            ],
        ),
        migrations.AddField(
            model_name='citizen',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='izuminapp.player'),
        ),
        migrations.AddField(
            model_name='player',
            name='nation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='player_nation', to='izuminapp.nation'),
        ),
        migrations.AddField(
            model_name='player',
            name='town',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='player_town', to='izuminapp.town'),
        ),
    ]
