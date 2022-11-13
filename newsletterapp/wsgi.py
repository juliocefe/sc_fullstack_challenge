"""
WSGI config for newsletterapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior
# newsletterapp directory.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "newsletterapp"))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsletterapp.settings')

application = get_wsgi_application()
