# Generated by Django 3.2.8 on 2022-09-15 21:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('location', models.CharField(max_length=255)),
                ('cinemas_picture', models.ImageField(blank=True, null=True, upload_to='cinemas_pictures')),
                ('contacts', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('movie_image', models.ImageField(upload_to='movies_images')),
                ('age_limit', models.IntegerField(blank=True, null=True)),
                ('beginning_of_movie', models.DateField(blank=True, null=True)),
                ('ending_of_movie', models.DateField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoviesCategory',
            fields=[
                ('slug', models.SlugField(max_length=150, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('cinemas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.cinemas')),
            ],
        ),
        migrations.CreateModel(
            name='RoomsFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.moviescategory')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movies')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.rooms')),
            ],
        ),
        migrations.AddField(
            model_name='rooms',
            name='format',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.roomsformat'),
        ),
        migrations.AddField(
            model_name='movies',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.moviescategory'),
        ),
    ]
