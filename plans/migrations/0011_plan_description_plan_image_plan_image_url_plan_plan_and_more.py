# Generated by Django 4.0 on 2022-01-02 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0010_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='plan',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='plan',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Plans', to='plans.plan'),
        ),
        migrations.AddField(
            model_name='plan',
            name='price',
            field=models.DecimalField(
                decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='rating',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
