# Generated by Django 4.2.4 on 2023-09-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product01', '0002_alter_product_category_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_url',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
