# Generated by Django 3.2.13 on 2022-05-21 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateTimeField(auto_now_add=True)),
                ('checkout', models.DateTimeField(blank=True, null=True)),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='rental.rental')),
            ],
        ),
    ]
