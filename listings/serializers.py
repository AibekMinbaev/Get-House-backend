from rest_framework import serializers
from .models import Listing 


class PropertySerializer(serializers.HyperlinkedModelSerializer): #TODO: Add user later. 
    class Meta:
        model = Listing 
        fields = ('id', 'title', 'price', 'num_bedrooms', 'num_bathrooms', 'square_footage', 'city', 'address', 'property_image') 
