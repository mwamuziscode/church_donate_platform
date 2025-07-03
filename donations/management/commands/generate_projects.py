from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from donations.models
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate fake Categories, Users, and Projects for testing.'
""" 
    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write("🔧 Generating fake data...")

        # Create Categories
        categories = []
        for _ in range(5):
            name = fake.unique.word().capitalize()
            category = Category.objects.create(
                name=name,
                description=fake.sentence()
            )
            categories.append(category)
        self.stdout.write("✅ Created Categories.")

        # Create Users
        users = []
        for _ in range(10):
            username = fake.unique.user_name()
            user = User.objects.create_user(
                username=username,
                email=fake.email(),
                password="password123",
                first_name=fake.first_name(),
                last_name=fake.last_name()
            )
            users.append(user)
        self.stdout.write("✅ Created Users.")

        # Create Projects
        for _ in range(10):
            name = fake.company()
            project = Project.objects.create(
                name=name,
                project_key=fake.unique.bothify(text='???-####'),
                category=random.choice(categories),
                project_lead=random.choice(users),
                project_status=random.choice(['active', 'inactive']),
                project_description=fake.paragraph(),
                project_urls=fake.url(),
                slug=slugify(name)
            )
            members = random.sample(users, k=random.randint(1, len(users)))
            project.project_members.set(members)
            project.save()
        self.stdout.write("✅ Created Projects.")

        self.stdout.write(self.style.SUCCESS("🎉 Done generating fake data."))
"""