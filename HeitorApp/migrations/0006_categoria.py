# Generated by Django 5.0.3 on 2024-03-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeitorApp', '0005_produto_cor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_produto', models.CharField(max_length=20)),
            ],
        ),
    ]
