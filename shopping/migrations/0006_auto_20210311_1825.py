# Generated by Django 3.1.5 on 2021-03-11 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20210311_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.product_category', to_field='sub_pro_category'),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='pro_category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='sub_pro_category',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]