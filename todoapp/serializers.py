from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo 
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'done_at', 'deleted_at', )

    def validate_status(self, value):
        if value < 0:
            raise serializers.ValidationError('Status no negative')
        return value