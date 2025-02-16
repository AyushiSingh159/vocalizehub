from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from speechify import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('generate-speech/', views.generate_speech, name='generate_speech'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

