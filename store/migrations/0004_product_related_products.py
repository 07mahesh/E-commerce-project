# Generated by Django 5.1.7 on 2025-03-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(blank=True, related_name='related_to', to='store.product'),
        ),
    ]
