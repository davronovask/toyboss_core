# Generated by Django 5.1.2 on 2024-10-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_aboutme_image_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]