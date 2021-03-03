from django.db import models
from django.contrib.auth.models import User

# User model implemented by using proxy method
# (Extending from django user model)
class Profile(models.Model):

    # Relationship with User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Profile fields
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    # media field
    picture = models.ImageField(upload_to="users/pictures", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # For console tests purposes
    def __str__(self):
        return self.user.username
