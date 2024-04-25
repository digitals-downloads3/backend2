from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
def validate_only_none_instance(obj):
	model = obj.__class__
	if(model.objects.count() > 0 and obj.id != model.objects.get().id):
		raise ValidationError('This section can Create only one time') 	


class Category(models.Model):
    STATUS_CHOICES= (
        ('d', 'draft'),
        ('p', 'publish')
    )

    title = models.CharField(max_length=250)
    position = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    class Meta:
        verbose_name_plural = 'categoreis'

    def __str__(self):
        return self.title


class Book(models.Model):
    STATUS_CHOICES= (
        ('d', 'draft'),
        ('p', 'publish')
    )
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    about  = models.TextField()
    description = models.TextField()
    photo = models.ImageField(upload_to='images')
    additional_information = models.TextField()
    publish = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    is_featured = models.BooleanField(default=False, verbose_name="Is Featured ?")

    class Meta:
        verbose_name_plural = 'books'
        ordering = ['-publish']

    def __str__(self):
        return self.title
    

class BookOfTheDay(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


    def clean(self):
        validate_only_none_instance(self)

    def __str__(self):
        return 'Book Of The Day'
    
    class Meta:
        verbose_name_plural = 'Book Of The Day'



class QuoteOfTheDay(models.Model):
    author = models.CharField(max_length=250)
    description = models.TextField()

    def clean(self):
        validate_only_none_instance(self)

    def __str__(self):
        return self.author
    
    class Meta:
        verbose_name_plural = 'Quote Of The Day'
    

class Article(models.Model):
    STATUS_CHOICES= (
        ('d', 'draft'),
        ('p', 'publish')
    )
    title = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(upload_to='images', null=True)
    decsription = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = 'Articles'
        ordering = ['-publish']



class AboutUs(models.Model):
    decsription = models.TextField(null=True)
    number = models.TextField(null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return 'About Us'
    

    class Meta:
        verbose_name_plural = 'About Us'