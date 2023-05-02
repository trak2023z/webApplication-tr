# Generated by Django 4.1.7 on 2023-04-18 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ogloszenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=9)),
                ('opis', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Zdjecie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zdjecie', models.ImageField(upload_to='')),
                ('ogloszenie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacjaogloszeniowa.ogloszenie')),
            ],
        ),
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefon', models.CharField(max_length=9)),
                ('miejscowosc', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Podkategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacjaogloszeniowa.kategoria')),
            ],
        ),
        migrations.AddField(
            model_name='ogloszenie',
            name='podkategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacjaogloszeniowa.podkategoria'),
        ),
        migrations.AddField(
            model_name='ogloszenie',
            name='uzytkownik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacjaogloszeniowa.uzytkownik'),
        ),
    ]