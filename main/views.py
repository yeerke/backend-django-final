from rest_framework import viewsets
from .models import Book, Journal
from rest_framework.response import Response
from .serializers import BookSerializer, JournalSerializer

class BookViewSet(viewsets.ViewSet):

    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, many=False)

        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class JournalViewSet(viewsets.ViewSet):

    def list(self, request):
        journals = Journal.objects.all()
        serializer = JournalSerializer(journals, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        journal = Journal.objects.get(id=pk)
        serializer = JournalSerializer(journal, many=False)

        return Response(serializer.data)

    def create(self, request):
        serializer = JournalSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
