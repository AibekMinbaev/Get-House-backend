from .models import Listing 

from .serializers import * 
from rest_framework import viewsets 

class PropertyViewSet(viewsets.ModelViewSet): 
    """
    API endpoint that allows properties to be views or edited
    """
    serializer_class = PropertySerializer
    queryset = Listing.objects.all()
