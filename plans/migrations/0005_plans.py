# Generated by Django 4.0 on 2022-01-01 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_delete_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(
                    decimal_places=2, max_digits=6, null=True)),
                ('rating', models.DecimalField(blank=True,
                 decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(
                    blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('friendly_name', models.CharField(
                    blank=True, max_length=254, null=True)),
                ('category', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to='plans.category')),
            ],
        ),
    ]
