from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    """
    A ViewSet for performing CRUD operations on the Book model.
    Only authenticated users can access this API.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]







import re

def check_modelviewset(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Check for ModelViewSet import
        if "from rest_framework.viewsets import ModelViewSet" not in content:
            return "Error: ModelViewSet is not imported."

        # Check for a class inheriting from ModelViewSet
        pattern = r"class\s+\w+\s*\(\s*ModelViewSet\s*\):"
        if not re.search(pattern, content):
            return "Error: No class extends ModelViewSet in api/views.py."

        # Check for queryset and serializer_class attributes
        if "queryset" not in content or "serializer_class" not in content:
            return "Error: queryset or serializer_class is missing in the ViewSet."

        return "Success: ViewSet with ModelViewSet is correctly implemented."

    except FileNotFoundError:
        return "Error: The file 'api/views.py' was not found."

# Path to api/views.py
file_path = "api/views.py"
print(check_modelviewset(file_path))








