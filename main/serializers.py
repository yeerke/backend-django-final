from rest_framework import serializers
from .models import Book, Journal

class BookSerializer(serializers.ModelSerializer):
    class Meta():
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book

class JournalSerializer(serializers.ModelSerializer):
    class Meta():
        model = Journal
        fields = '__all__'

    def create(self, validated_data):
        journal = Journal.objects.create(**validated_data)
        return journal
