# Generated by Django 5.0.3 on 2024-03-30 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_product_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
