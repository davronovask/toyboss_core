# Generated by Django 5.1.2 on 2024-10-29 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0017_product_composition'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='instructions',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]