# Generated by Django 3.0 on 2022-11-07 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_writes', models.DateField()),
                ('nr_order', models.IntegerField()),
                ('tape_of_delivery', models.CharField(choices=[('P', 'P'), ('C', 'C')], default='C', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.IntegerField()),
                ('name', models.CharField(max_length=26)),
                ('quantity', models.IntegerField()),
                ('quantity_not_damaget', models.IntegerField()),
                ('quantity_damage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SkuName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.IntegerField()),
                ('name_of_produckt', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gen_protocol.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gen_protocol.Product')),
            ],
        ),
    ]
