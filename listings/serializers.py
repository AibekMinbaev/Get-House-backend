from rest_framework import serializers
from .models import Listing 


class ListingSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Listing 
        fields = ('id', 'title', 'price', 'num_bedrooms', 'num_bathrooms', 'square_footage', 'state', 'city', 'street', 'address') 
