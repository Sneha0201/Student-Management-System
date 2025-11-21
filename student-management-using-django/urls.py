"""Student_Management_System URL Configuration

The `urlpatterns` list routes URLs to views.
Examples:
Functional views 
1. Add an import: from my_app import views
2. Add a URL to urlpatterns: path('', Home.as_view(), name = 'home')
Class-based views
1. Add an import: from other_app.views import Home
2. Add a URL to urlpatterns: path('', Home.as_views(), name = 'home')
Including another URLconf
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path("", include('main_app.urls')),
    path("accounts/", include("django.conrib.auth.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)