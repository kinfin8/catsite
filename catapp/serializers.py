from rest_framework import serializers

from .models import Breed
from .models import Cat
from .models import Human
from .models import Home


class CatOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = [
            'id',
            'name',
        ]


class CatHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = [
            'id',
            'name',
        ]


class BreedSerializer(serializers.ModelSerializer):
    cats_owners = serializers.SerializerMethodField()
    cats_homes = serializers.SerializerMethodField()

    def get_cats_owners(self, obj):
        # cat_owner = Human.objects.filter(cats__in=obj.cats.all()).values('id', 'name')
        cat_owner = Human.objects.filter(cats__breed_id=obj.id)
        serializer = CatOwnerSerializer(cat_owner, many=True)
        return serializer.data
    
    def get_cats_homes(self, obj):
        # cat_owner = Human.objects.filter(cats__in=obj.cats.all()).values('home')
        # cat_home = Home.objects.filter(id__in=cat_owner.all())
        cat_home = Home.objects.filter(human__cats__breed_id=obj.id)
        serializer = CatHomeSerializer(cat_home, many=True)
        return serializer.data

    class Meta:
        model = Breed
        fields = [
            'id',
            'name',
            'origin',
            'description',
            'cats',
            'cats_owners',
            'cats_homes',
        ]


class CatSerializer(serializers.ModelSerializer):
    breed_name = serializers.CharField(source="breed.name", read_only=True)
    owner_name = serializers.CharField(source="owner.name", read_only=True)
    home = serializers.IntegerField(source="owner.home.id", read_only=True)
    home_name = serializers.CharField(source="owner.home.name", read_only=True)

    class Meta:
        model = Cat
        fields = [
            'id',
            'name',
            'gender',
            'date_of_birth',
            'description',
            'breed',
            'breed_name',
            'owner',
            'owner_name',
            'home',
            'home_name',
        ]


class CatNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = [
            'name',
        ]


class HumanSerializer(serializers.ModelSerializer):
    cats_names = serializers.SerializerMethodField()
    home_name = serializers.CharField(source="home.name", read_only=True)

    def get_cats_names(self, obj):
        cat_names = Cat.objects.filter(id__in=obj.cats.all()).values('name')
        serializer = CatNameSerializer(cat_names, many=True)
        return serializer.data

    class Meta:
        model = Human
        fields = [
            'id',
            'name',
            'gender',
            'date_of_birth',
            'description',
            'cats',
            'cats_names',
            'home',
            'home_name',
        ]


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = [
            'id',
            'name',
            'address',
            'building_type',
        ]