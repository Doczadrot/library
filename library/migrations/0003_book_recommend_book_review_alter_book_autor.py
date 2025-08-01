# Generated by Django 5.2.1 on 2025-07-19 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='recommend',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.autor', verbose_name='books'),
        ),
    ]
