from django.db import models
from faker import Faker
from ckeditor.fields import RichTextField
# RichTextUploadingField()  #
from ckeditor_uploader.fields import RichTextUploadingField


fake = Faker()


class Topic(models.Model):
    name = models.CharField(blank=False,max_length=255, default=fake.sentence(nb_words=10))
    image = models.ImageField(default="default.jpg", blank=False, max_length=255)
    descriptions = models.TextField(blank=True, default=fake.sentence(nb_words=20))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    # add url field to the image field default fake.image.urlPicsumPhotos({ blur: 4, grayscale: true })
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return "default.jpg"



class HeadLine(models.Model):
    front_line = models.CharField( max_length=255,  blank=False,  default=fake.sentence(nb_words=20))
    descriptions = models.CharField(max_length=255, blank=False, default=fake.sentence(nb_words=20))
    image = models.ImageField(default="default.jpg", blank=False, max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.front_line.istitle()

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(help_text="Write Content That Are well study")
    created_at = models.DateTimeField(auto_now_add=True)
    cats = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='blogs', blank=False) 
    image = models.ImageField(default="default.jpg", blank=False, max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    update = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    update = models.ForeignKey(Blog, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)



class Donation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_charge_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
