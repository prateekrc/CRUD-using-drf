from django.urls import path,include
from student import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('hm', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    path("st/<int:pk>",views.show,name="show"),
    path("stdet",views.st_details,name="st_des"),

   ]
