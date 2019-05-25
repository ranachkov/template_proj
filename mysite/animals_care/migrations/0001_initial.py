# Generated by Django 2.2.1 on 2019-05-24 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_auto_20190523_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfileOwner')),
            ],
        ),
        migrations.CreateModel(
            name='Other_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='animals_care.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('image_url', models.URLField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('company', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='animals_care.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfileOwner')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('breed', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('age', models.PositiveIntegerField()),
                ('image_url', models.URLField()),
                ('kind', models.CharField(blank=True, choices=[('D', 'Dog'), ('C', 'Cat')], max_length=1)),
                ('favorite_food', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='animals_care.Food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfileOwner')),
            ],
        ),
    ]
