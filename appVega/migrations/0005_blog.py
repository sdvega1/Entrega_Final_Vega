# Generated by Django 4.0.5 on 2022-07-20 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVega', '0004_fixture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('cuerpo', models.CharField(max_length=100)),
            ],
        ),
    ]
