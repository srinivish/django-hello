# greetings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
]

# helloapp/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('greetings.urls')),
]
