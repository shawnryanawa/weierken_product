# Generated by Django 4.2.4 on 2023-09-01 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product01', '0003_alter_product_image_url_alter_product_product_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='lead_time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='order',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sample_time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]