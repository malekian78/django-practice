from django.core.management.base import BaseCommand
from faker import Faker
from django.utils import timezone
import random
from accounts.models import User
from todo.models import Task

class Command(BaseCommand):
    help = "inserting 5 task data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker("fa_IR")
        
    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(), password="Test@123456", is_active=True)

        for _ in range(5):
            Task.objects.create(
                user=user,
                title=self.fake.sentence(nb_words = 6),
                complete=random.choice([True, False]),
            )