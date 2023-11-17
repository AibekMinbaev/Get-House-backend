from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers  

from django.conf import settings 
from django.conf.urls.static import static 

#Importing views 
from . import views as main_views 
from users import views as user_views
from listings import views as listings_views 


#API urls
router = routers.DefaultRouter()
router.register(r'properties', listings_views.PropertyViewSet, "properties")


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

    path('messages/', user_views.messages_page),
    path('messages/<pk>/', user_views.messages_detail), 

    path('contactus/', user_views.contactus_create), 
]


# Main url patterns 
urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", include(admin_patterns)), 

    path('user/', include(user_patterns)),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
