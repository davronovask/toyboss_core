# Generated by Django 5.1.2 on 2024-10-29 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0018_recipes_instructions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='instructions',
            new_name='directions',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='product',
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredients',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipes',
            name='categories',
            field=models.ManyToManyField(to='market.productcategory'),
        ),
    ]
