# Generated by Django 4.0.1 on 2022-01-13 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]