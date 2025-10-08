from rest_framework import serializers
from .models import Book, Author, Genre, Publishment


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PublishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishment
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    publishment = serializers.PrimaryKeyRelatedField(queryset=Publishment.objects.all())

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):

        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance