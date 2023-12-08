from rest_framework import generics
from .models import Librarian
from .serializers import LibrarianSerializer

class LibrarianCreateAPIView(generics.CreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer


class LibrarianRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer


class LibrarianUpdateAPIView(generics.UpdateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer


class LibrarianDeleteAPIView(generics.DestroyAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

class LibrarianListAPIView(generics.ListAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
