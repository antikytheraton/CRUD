from rest_framework import serializers
from .models import Restaurant, Menu, Product


class ProdSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class MenuSer(serializers.ModelSerializer):
    products = ProdSer(many=True, read_only=True)
    class Meta:
        model = Menu
        fields = '__all__'


class RestaurantSer(serializers.ModelSerializer):
    menus = MenuSer(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = '__all__'


