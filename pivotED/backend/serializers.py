from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from . import models

class TicketSerializer(serializers.ModelSerializer):
    tags = serializers.ChoiceField([
        'bug',
        'important',
        'update',
        'announcement',
        'news'
    ])

    class Meta:
        model = models.Ticket
        fields = '__all__'
        