from django.contrib import admin
from django.urls import path, include 

from django.conf import settings 
from django.conf.urls.static import static 

from . import views as main_views 
from users import views as user_views
from listings import views as listings_views 
from staff import views as staff_views 

#Admin url patterns 
admin_patterns = [
    path('', admin.site.urls),
    path('logout/', user_views.logout_user),
]

#Users url patterns 
user_patterns = [
    path('register/',user_views.register), 
    path('login/', user_views.login_user),
    path('logout/', user_views.logout_user),

    path('profile/', user_views.profile_page),
    path('profile/edit/', user_views.profile_edit),
    path('properties/', user_views.my_properties),

    path('messages/', staff_views.messages_page),
    path('messages/<pk>/', staff_views.messages_detail), 

    path('contactus/', user_views.contactus_create), 
]

#Property url patterns
property_patterns = [
    path('all/', listings_views.listing_list),
    path('single/<pk>/', listings_views.listing_retrieve ),
    path('create/', listings_views.listing_create), 
    path('single/<pk>/update/', listings_views.listing_update),
    path('single/<pk>/delete/', listings_views.listing_delete), 
    path('rent/all/', listings_views.listing_rent_list), 
    path('rent/single/<pk>/', listings_views.listing_rent),
]

# Main url patterns 
urlpatterns = [
    path("", main_views.home_view), 
    path('aboutus/', main_views.aboutus),

    path("admin/", include(admin_patterns)), 
    path('user/', include(user_patterns)),
    path('property/', include(property_patterns)),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

      