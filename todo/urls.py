from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from todo import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='tasks/')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tasks/', include('tasks.urls')),
    path('accounts/register/', views.register, name='register'),
]
