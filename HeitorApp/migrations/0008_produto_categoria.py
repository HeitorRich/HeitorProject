# Generated by Django 5.0.3 on 2024-03-26 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeitorApp', '0007_rename_nome_do_produto_categoria_nome_da_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HeitorApp.categoria'),
        ),
    ]