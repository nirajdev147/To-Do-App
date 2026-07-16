import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# We use @login_required(login_url=...) or skip it entirely to keep assets public
def serve_bootstrap(request):
    css_path = os.path.join(settings.BASE_DIR, 'static', 'css', 'bootstrap.min.css')
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type="text/css")
    except FileNotFoundError:
        # Fallback if the path is slightly shifted inside the main app folder
        css_path = os.path.join(settings.BASE_DIR, 'todo', 'static', 'css', 'bootstrap.min.css')
        with open(css_path, 'r', encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type="text/css")

urlpatterns = [
    # This MUST sit at the very top of the list so it intercepts the asset request first!
    path('static/css/bootstrap.min.css', serve_bootstrap),
    
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  
    path('accounts/', include('django.contrib.auth.urls')),  
]
