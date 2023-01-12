from rest_framework import serializers
from .models import Car # Can use .filename if you are importing from the same parent file our car model and serializer file are both in Cars folder

class CarSerializer(serializers.ModelSerializer): # Set class to app name + serializer
    class Meta: # Where we define small bits of information about serializer class
        model = Car #what model this serializer should be bound to (in this case the Car model)
        fields = ['id', 'make', 'model', 'year', 'price'] # What column are in the model what you can see