from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Team 
        fields = [
            'id', 'owner', 'created_at', 'name', 'image', 'is_owner'
        ]
