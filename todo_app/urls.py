"""
URL configuration for todo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponse

# A direct backup view that reads your Bootstrap file and forces the correct MIME type
def serve_bootstrap(request):
    css_path = os.path.join(settings.BASE_DIR, 'static', 'css', 'bootstrap.min.css')
    with open(css_path, 'r', encoding='utf-8') as f:
        return HttpResponse(f.read(), content_type="text/css")

urlpatterns = [
    # Force-routes the exact broken path directly to our custom handler
    path('static/css/bootstrap.min.css', serve_bootstrap),
    
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  
    path('accounts/', include('django.contrib.auth.urls')),  
]
