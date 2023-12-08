from django.urls import path
from .views import author_view,author_view_with_id

urlpatterns = [
  path('',author_view),
  path('<int:id>/',author_view_with_id),
]