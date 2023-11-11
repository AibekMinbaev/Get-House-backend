from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from listings.filters import BuyFilter
from rest_framework import viewsets 
from listings.serializers import ListingSerializer 
from listings.models import Listing


def home_view(request): 
    if request.method == "POST":
        price = request.POST.get('price')
        num_bedrooms = request.POST.get('num_bedrooms')
        num_bathrooms = request.POST.get('num_bathrooms')
        
        request.session['filter_data'] = {'price':price, 'num_bedrooms':num_bedrooms, 'num_bathrooms':num_bathrooms}
        return redirect('/listings/all/')
    
    buy_filter = BuyFilter()
    context = {'buy_filter':buy_filter} 
    return render(request, "home_page.html", context)   


class test_view(viewsets.ModelViewSet): 
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

