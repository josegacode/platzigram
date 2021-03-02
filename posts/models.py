from django.db import models

# A model is a structure which let us
# manage the DB
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    bio = models.TextField(blank=True)

    is_admin = models.BooleanField(default=False)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)