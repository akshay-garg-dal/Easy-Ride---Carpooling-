from django.urls import include, path
from main import views

urlpatterns = [

    path('', include('rest_framework.urls')),
    path("test", views.test),
    path("users", views.get_all_users),

]