from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404
from .serializers import RestaurantSer, MenuSer, ProdSer
from .models import Restaurant, Menu, Product


# class RestaurantView(generics.ListCreateAPIView):
#     serializer_class = RestaurantSer
#     queryset = Restaurant.objects.all()

class RestaurantView(APIView):
    
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        restaurant = request.data
        serializer = RestaurantSer(data=restaurant)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class RestaurantDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = RestaurantSer
#     queryset = Restaurant.objects.all()
class RestaurantDetailsView(APIView):
    
    def get(self, request, pk):
        # try:
        #     restaurant = Restaurant.objects.get(id=pk)
        # except Restaurant.DoesNotExist:
        #     raise Http404
        restaurant = get_object_or_404(Restaurant, id=pk)
        serializer = RestaurantSer(restaurant)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        restaurant = get_object_or_404(Restaurant, id=pk)
        serializer = RestaurantSer(restaurant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restaurant = get_object_or_404(Restaurant, id=pk)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MenuView(generics.ListCreateAPIView):
    serializer_class = MenuSer
    queryset = Menu.objects.all()

class MenuDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSer
    queryset = Menu.objects.all()