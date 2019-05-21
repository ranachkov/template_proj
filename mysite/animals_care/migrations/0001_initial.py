# Generated by Django 2.2.1 on 2019-05-21 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('breed', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('age', models.PositiveIntegerField()),
                ('image_url', models.URLField()),
                ('favorite_food', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='animals_care.Food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ProfileOwner')),
            ],
        ),
    ]
