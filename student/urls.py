from django.urls import path,include
from student import views
from rest_framework import routers
# from rest_framework.routers import DefaultRouter
# from student.views import UserViewSet
router = routers.DefaultRouter()
router.register(r'users/', views.UserViewSet)


urlpatterns = [
    path('hm', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path("st/<int:pk>",views.show,name="show"),
    path("stdet",views.st_details,name="st_des"),
    
    path("set",views.UserViewSet2.as_view(),name="st_des"),
    path("ptdel/<int:id>",views.UserViewSet3.as_view(),name="sdes")

   ]
