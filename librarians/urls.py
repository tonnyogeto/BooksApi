from django.urls import path
from .views import LibrarianCreateAPIView,LibrarianDeleteAPIView,LibrarianRetrieveAPIView,LibrarianUpdateAPIView,LibrarianListAPIView

urlpatterns = [
    path("create/", LibrarianCreateAPIView.as_view()),
    path("retrieve/<pk>/",LibrarianRetrieveAPIView.as_view()),
    path("update/<pk>/",LibrarianUpdateAPIView.as_view() ),
    path("delete/<pk>/", LibrarianDeleteAPIView.as_view()),
    path("list/", LibrarianListAPIView.as_view())
]