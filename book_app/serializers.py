from rest_framework import serializers
from .models import Book, Author, Genre, Publishment


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
    
    
class PublishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishment
        fields = ['id', 'name', 'address']

    def create(self, validated_data):
        return Publishment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer()
    publishment = PublishmentSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'publishment', 'published_date', 'isbn']

    
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        genre_data = validated_data.pop('genre')
        publishment_data = validated_data.pop('publishment')

        author, _ = Author.objects.get_or_create(**author_data)
        genre, _ = Genre.objects.get_or_create(**genre_data)
        publishment, _ = Publishment.objects.get_or_create(**publishment_data)

        book = Book.objects.create(author=author, genre=genre, publishment=publishment, **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        genre_data = validated_data.pop('genre', None)
        publishment_data = validated_data.pop('publishment', None)

        if author_data:
            author, _ = Author.objects.get_or_create(**author_data)
            instance.author = author

        if genre_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            instance.genre = genre

        if publishment_data:
            publishment, _ = Publishment.objects.get_or_create(**publishment_data)
            instance.publishment = publishment

        instance.title = validated_data.get('title', instance.title)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.save()
        return instance