from django.urls import path
from .views import FirstView, SecondView

urlpatterns = [
    path('',FirstView.as_view),
    path('<int:id>',SecondView.as_view)
]