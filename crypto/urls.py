from crypto import views
from django.urls import path

urlpatterns = [
    path("", views.home,name="home" ),
    path("prices/", views.prices,name="prices" ),
]
