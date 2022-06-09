from django.shortcuts import render
from rest_framework import viewsets
from .models import Lead
from .serializers import LeadSerializer
from team.models import Team

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        
        serializer.save(team=team, created_by=self.request.user)