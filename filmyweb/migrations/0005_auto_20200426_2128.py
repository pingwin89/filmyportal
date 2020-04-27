# Generated by Django 3.0.5 on 2020-04-26 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0004_auto_20200426_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (1, 'Horror'), (4, 'Drama'), (3, 'Sci-fi'), (2, 'Komedia')], default=0),
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.TextField(blank=True, default='')),
                ('gwiazdki', models.PositiveSmallIntegerField(default=5)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmyweb.Film')),
            ],
        ),
    ]
