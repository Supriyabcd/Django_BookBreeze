# Generated by Django 5.1.1 on 2024-11-05 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_populate_booklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
