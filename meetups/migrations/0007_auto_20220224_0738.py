# Generated by Django 3.2.12 on 2022-02-24 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0006_auto_20220224_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='meetups',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetups.location'),
        ),
    ]
