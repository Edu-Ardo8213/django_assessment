# Generated by Django 4.1.3 on 2023-02-23 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_alter_customers_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrators',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]