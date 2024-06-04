from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name="main"),
    path('test_path/<slug:slug_id>', views.test_path, name="test_path"),
]
# AAAAAAAAAAAAAAAAAAAAAAAAA YAAAAAAAAAA USTAAAAAAAAAAAAAAAAAAAAAAAAAAAAL