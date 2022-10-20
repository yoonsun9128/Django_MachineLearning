from django.urls import path
from . import views
from Django_AI.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

app_name = 'tweet'

urlpatterns = [
    path("", views.home, name='home'),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)