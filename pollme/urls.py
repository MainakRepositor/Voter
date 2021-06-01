
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('polls/', include('polls.urls', namespace="polls")),
    path('accounts/', include('accounts.urls', namespace="accounts")),
]
