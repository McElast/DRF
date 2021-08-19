from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField('get_cost')

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity', 'measure', 'total_cost', 'date_mod']

    def get_cost(self, obj):
        res = obj.price * obj.quantity
        return res

