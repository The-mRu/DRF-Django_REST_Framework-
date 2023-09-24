from rest_framework import serializers
from .models import demo

class demoSerializer(serializers.Serializer):
    Name =serializers.CharField(max_length=30)
    course_name = serializers.CharField(max_length=30)
    course_duration =serializers.IntegerField()
    seat=serializers.IntegerField()

    def create(self, validated_data ):
        return demo.objects.create(**validated_data)
        
    def update(self, instance, validated_data): 
        # instance-->store previous data /works with previous data
        #validated_data--> handling updated data
        instance.Name=validated_data.get('Name',instance.Name)
        instance.course_name=validated_data.get('course_name',instance.course_name)
        instance.course_duration=validated_data.get('course_duration',instance.course_duration)
        instance.seat=validated_data.get('seat',instance.seat)
        
        instance.save()
        return instance