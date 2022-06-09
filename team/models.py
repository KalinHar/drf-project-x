from django.contrib.auth.models import User
from django.db import models

class Team(models.Model):
    # PLAN_ACTIVE = 'active'
    # PLAN_CANCELLED = 'cancelled'

    # CHOICES_PLAN_STATUS = (
    #     (PLAN_ACTIVE, 'Active'),
    #     (PLAN_CANCELLED, 'Cancelled')
    # )

    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # plan = models.ForeignKey(Plan, related_name='teams', on_delete=models.SET_NULL, null=True, blank=True)
    # plan_status = models.CharField(max_length=20, choices=CHOICES_PLAN_STATUS, default=PLAN_ACTIVE)
    # plan_end_date = models.DateTimeField(blank=True, null=True)
    # stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    # stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)