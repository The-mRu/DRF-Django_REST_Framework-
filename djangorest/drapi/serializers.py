from rest_framework import serializers
from .models import demo

class demoSerializer(serializers.Serializer):
    Name =serializers.CharField(max_length=30)
    course_name = serializers.CharField(max_length=30)
    course_duration =serializers.IntegerField()
    seat=serializers.IntegerField()

    def create(self, validated_data ):
        return demo.objects.create(**validated_data)
        