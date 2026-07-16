import os
from pathlib import Path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponse, Http404

def serve_bootstrap(request):
    """
    Scans the system dynamically to find bootstrap.min.css,
    preventing 500 errors if folders are slightly moved.
    """
    # 1. Search paths
    possible_paths = [
        os.path.join(settings.BASE_DIR, 'static', 'css', 'bootstrap.min.css'),
        os.path.join(settings.BASE_DIR, 'todo_app', 'static', 'css', 'bootstrap.min.css'),
        os.path.join(settings.BASE_DIR, 'todo', 'static', 'css', 'bootstrap.min.css'),
        os.path.join(settings.BASE_DIR, 'staticfiles', 'css', 'bootstrap.min.css'),
    ]
    
    # 2. Dynamic search fallback
    for path_str in possible_paths:
        if os.path.exists(path_str):
            with open(path_str, 'r', encoding='utf-8') as f:
                return HttpResponse(f.read(), content_type="text/css")
                
    # 3. Last resort scan
    for root, dirs, files in os.walk(settings.BASE_DIR):
        if 'bootstrap.min.css' in files:
            file_path = os.path.join(root, 'bootstrap.min.css')
            with open(file_path, 'r', encoding='utf-8') as f:
                return HttpResponse(f.read(), content_type="text/css")

    # If it absolutely does not exist anywhere on the server drive
    raise Http404("Bootstrap CSS file could not be found anywhere in the workspace.")

urlpatterns = [
    # Intercepts the browser before any auth or app views can block it
    path('static/css/bootstrap.min.css', serve_bootstrap),
    
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  
    path('accounts/', include('django.contrib.auth.urls')),  
]
