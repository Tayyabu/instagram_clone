import os
import random
from random import choice
import django
from faker import Faker
# Replace 'your_project_name' with the actual name of your project's settings module folder
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instagram_clone.settings")
django.setup()

# Now you can import your Django models
from accounts.models import User
from core.models import Post,Comment

fake = Faker()

def create_fake_data(n=10):
    for _ in range(n):
        content = fake.paragraph(2)
        author = choice(list(User.objects.filter(pk__in=[user.id for user in User.objects.all()]))) # type: ignore
        post = choice(list(Post.objects.filter(pk__in=[post.id for post in Post.objects.all()]))) # type: ignore
       
    
      
    print(f"Created {n} fake records.")

if __name__ == '__main__':
    create_fake_data(100) # Creates 20 fake records
