from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard/')),  # Redirect root to dashboard
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),  # Include tracker app URLs
]
