from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer,MatchTableSerializer, RoleSerializer, MessageSerializer
from .models import User,MatchTable,Role,Message

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class MatchTableView(viewsets.ModelViewSet):
    serializer_class = MatchTableSerializer
    queryset = MatchTable.objects.all()

class MessageView(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()    

class RoleView(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()        

 