from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from donations.models import Blog,  Topic, Comment, Donation
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate fake Categories, Users, and Projects for testing.'

    def handle(self, *args, **kwargs):

        # delete all existing data
        User.objects.all().delete()
        Topic.objects.all().delete()
        Blog.objects.all().delete()
        Donation.objects.all().delete()
        Comment.objects.all().delete()
