# Generated by Django 3.0.8 on 2020-07-19 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200719_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='techspec',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.Product'),
        ),
        migrations.AlterField(
            model_name='techspec',
            name='attribute',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='techspec',
            name='value',
            field=models.CharField(max_length=64),
        ),
    ]
