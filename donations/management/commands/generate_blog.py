from operator import is_
from random import randint
from unicodedata import category
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from donations.models import Blog, Topic, HeadLine, Comment, Like, Donation
from faker import Faker
# from faker.providers import internet, person, address, company
import random

class Command(BaseCommand):
    help = 'Generate fake Bloges and Topics data for testing purposes.'
    # command: python manager.py create_tags


    def handle(self, *args, **kwargs):
        fake = Faker()
        # create all User fields

        for _ in range(10):
            topic = Topic.objects.create(
                name=fake.word(),
                image=fake.image_url(width=640, height=480)
            )
            topic.save()
            self.stdout.write(self.style.SUCCESS(f"🔍 Selected Topic: {topic.name}"))

            
        for _ in range(10):
            blog = Blog.objects.create(
                title=fake.sentence(nb_words=3),
                content=fake.text(max_nb_chars=200),
                created_at=fake.date_time_this_year(),
                cats = Topic.objects.order_by('?').first()  # Randomly select a topic,
            )
            blog.save()
            self.stdout.write(self.style.SUCCESS(f"🔍 Selected User: {blog.pk} - {blog.title}"))
        self.stdout.write(self.style.SUCCESS("🎉 Done generating fake data tags."))



