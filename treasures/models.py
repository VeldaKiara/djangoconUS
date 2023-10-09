from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField( 'email address', unique=True, blank=False, max_length = 254)

    class Meta:
        pass
    
    def __str__(self):
        return self.username
        # Specify unique related_names for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_users_groups',  # Unique related_name
        related_query_name='custom_user_group',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_users_permissions',  # Unique related_name
        related_query_name='custom_user_permission',
    )

class Treasure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name