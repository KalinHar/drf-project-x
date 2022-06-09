from django.contrib.auth.models import User
from django.db import models

from team.models import Team

class Client(models.Model):

    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    contact_person = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=250)
    website = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

