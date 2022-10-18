from django.urls import path
from . import views
from Django_AI.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home),
    path("home/", views.home, name='home')
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)