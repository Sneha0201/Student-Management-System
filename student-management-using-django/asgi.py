"""
ASGI config for Student_Management_System Project.
It exposes the ASGI callable as a module-level variable named ``application``.
"""
import os 
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Student_Management_System.settings')
application = get_asgi_application()