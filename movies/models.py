from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class MoviesCategory(models.Model):
    slug = models.SlugField(max_length=150, primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Cinemas(models.Model):
    name = models.CharField(max_length=150)
    opening_time = models.TimeField(auto_now_add=False)
    closing_time = models.TimeField(auto_now_add=False)
    location = models.CharField(max_length=255)
    cinemas_picture = models.ImageField(upload_to="cinemas_pictures", null=True, blank=True)
    contacts = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cinemas'
        verbose_name_plural = 'Cinemas'

class Movies(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    movie_image = models.ImageField(upload_to="movies_images")
    age_limit = models.IntegerField(blank=True, null=True)
    beginning_of_movie = models.DateTimeField(auto_now=False, blank=True, null=True)
    ending_of_movie = models.DateTimeField(auto_now=False, blank=True, null=True)
    category = models.ForeignKey(MoviesCategory, related_name='movies', on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Movies'
        verbose_name_plural = 'Movies'


class RoomsFormat(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Rooms(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    format = models.ForeignKey(RoomsFormat, on_delete=models.CASCADE)
    cinemas = models.ForeignKey(Cinemas, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    category = models.ForeignKey(MoviesCategory, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.start_time}"

