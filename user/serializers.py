from rest_framework import serializers
from .models import User,MatchTable,Role,Message



class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields =  "__all__"   


class UserSerializer(serializers.ModelSerializer):
    roles=serializers.CharField(read_only=True)
   

    class Meta:
        model = User
        fields =  "__all__"

class MatchTableSerializer(serializers.ModelSerializer):
    users1=serializers.CharField(read_only=True)
    users2=serializers.CharField(read_only=True)

    class Meta:
        model = MatchTable
        fields = "__all__"  

class MessageSerializer(serializers.ModelSerializer):
    matchtables=serializers.CharField(read_only=True)
    users3=serializers.CharField(read_only=True)

    class Meta:
        model = Message
        fields =  "__all__"  