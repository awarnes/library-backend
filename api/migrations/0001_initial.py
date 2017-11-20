# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 08:47
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('author', models.CharField(max_length=10000)),
                ('date_published', models.DateField(blank=True)),
                ('edition', models.CharField(blank=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Bookcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ManyToManyField(blank=True, to='api.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_loaned', models.DateField(blank=True)),
                ('expected_return_date', models.DateField(blank=True)),
                ('date_returned', models.DateField(blank=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('friends', models.ManyToManyField(related_name='_reader_friends_+', to='api.Reader')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=10000)),
                ('body', models.TextField(blank=True)),
                ('stars', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Reader')),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrower', to='api.Reader'),
        ),
        migrations.AddField(
            model_name='loan',
            name='loaner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loaner', to='api.Reader'),
        ),
        migrations.AddField(
            model_name='bookcase',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Reader'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Genre'),
        ),
    ]
