from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    different_products = queryset.count()
    serializer_class = ProductSerializer

    def list(self, request):
        query = self.get_queryset()
        different_products = query.count()
        serializer = ProductSerializer(query, many=True)
        return Response({'Всего товаров': different_products, 'Товары': serializer.data})

    def perform_create(self, serializer):
        serializer.save()


class ProductDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    different_products = queryset.count()
    serializer_class = ProductSerializer


class TotalCostView(APIView):
    def get(self, request):
        all_products_cost = 'Всего на складе товаров на сумму: ' \
                            + str(sum([prod.price * prod.quantity for prod in Product.objects.all()]))
        return Response(all_products_cost)

