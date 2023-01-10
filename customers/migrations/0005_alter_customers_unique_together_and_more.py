# Generated by Django 4.1.5 on 2023-01-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_rename_email_customers_correo_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customers',
            unique_together={('nombre_cliente', 'apellido_cliente')},
        ),
        migrations.AlterField(
            model_name='customers',
            name='correo',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
