# Generated by Django 3.2.7 on 2021-10-21 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('add_at', models.DateTimeField(auto_now_add=True)),
                ('sku', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazin.producte')),
            ],
        ),
    ]
