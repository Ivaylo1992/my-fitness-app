from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('myFitnessApp.food.urls')),
    path('accounts/', include('myFitnessApp.accounts.urls')),
]
