# Generated by Django 5.2.1 on 2025-05-27 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='discount_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='is_promotion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='promotional_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
