from unicodedata import category
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from norjiras.models.project_models import Category, Project
from faker import Faker
import random

from notes.views import cats

class Command(BaseCommand):
    help = 'Generate Projects'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            self.stdout.write("🔧 Generating fake data...")
            for _ in range(10):
                project_name = fake.unique.word().capitalize()
                #roject_key = f"{project_name[:3].upper()}{random.randint(100, 999)}{project_name[-2:].upper()}"
                category = Category.objects.order_by('?').first()
                if not category:
                    category = Category.objects.create(name=fake.word())
                    self.stdout.write(f"✅ Category created: {category.name}")

                project_lead = User.objects.order_by('?').first()
                if not project_lead:
                    project_lead = User.objects.create(
                        username=fake.user_name(),
                        email=fake.email(),
                        password=fake.password(),
                        first_name=fake.first_name(),
                        last_name=fake.last_name()
                    )
                    self.stdout.write(f"✅ Project lead created: {project_lead.username}")

                project_description = fake.text(max_nb_chars=200)
                project_urls = fake.url()

                project = Project.objects.create(
                    name=project_name,
                    #roject_key=f"{project_name[:3].upper()}{random.randint(100, 999)}#{project.id}{project_name[-2:].upper()}",
                    project_status=random.choice(['active', 'inactive']),
                    category=category,
                    project_lead=project_lead,
                    project_description=project_description,
                    project_urls=project_urls
                )

                project.slug = slugify(project.name)
                project.project_key = f"{project.name[:3].upper()}{project.id}{project.name[-2:].upper()}"
                project.save()

                self.stdout.write(self.style.SUCCESS(f"✅ Project '{project.name}' created with key '{project.project_key}'."))
        self.stdout.write(self.style.SUCCESS("🎉 Done generating fake data."))
