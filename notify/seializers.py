from rest_framework import serializers
from notify.models import Notify

class NotifySerializer(serializers.Serializer):
    id = UUIDField(format='hex_verbose')
    sender = serializers.EmailField(required=True, allow_blank=False, max_length=256)
    subject = serializers.TextField(required=True, allow_blank=False)
    message = serializers.TextField(required=True, allow_blank=False)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    authorize = serializers.BooleanField()
    count =  serializers.IntegerField()

    def create(self, data):
        return Notify.objects.create(**data)

    def update(self, instance, data):
        instance.sender = data.get('sender', instance.sender) 
        instance.subject = data.get('subject', instance.subject)
        instance.message = data.get('message', instance.message)
        instance.authorize = data.get('authorize', instance.authorize) 
        instance.count = data.get('count', instance.count)

        instance.save()
        return instance