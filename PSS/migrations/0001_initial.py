# Generated by Django 3.0.8 on 2020-09-07 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hub_name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=500)),
                ('address', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('contrib', models.FloatField(default=0.0)),
                ('consume', models.FloatField(default=0.0)),
                ('usage_stat', models.FloatField(default=0.0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('install_cost', models.FloatField(default=0.0)),
                ('life_span', models.IntegerField(default=25)),
                ('hub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Hub')),
            ],
        ),
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load_name', models.CharField(max_length=100)),
                ('essential', models.BooleanField(default=True)),
                ('hub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PSS.Hub')),
            ],
        ),
    ]