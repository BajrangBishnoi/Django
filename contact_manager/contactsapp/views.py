from django.shortcuts import render
from .models import Contact
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import Contactserializer, AddContactSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_all(request):
    query = Contact.objects.all()
    serializer = Contactserializer(query, many=True, context={'request':request})
    return Response(serializer.data)

@api_view(['POST'])
def add_contact(request):
    print(request.data)
    serializer = Contactserializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def edit_contact(request, pk):
    query = get_object_or_404(Contact, pk=pk)
    serializer = Contactserializer(query, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_contact(request, pk):
    query = get_object_or_404(Contact, pk=pk)
    query.delete()
    return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def search(request):
    search_query = request.data.get('search')
    print(search_query)
    if search_query:
        query = Contact.objects.filter(
        Q(name__icontains=search_query) |  # Searching in the 'name' field
        Q(type__icontains=search_query) |  # Searching in the 'type' field
        Q(number__icontains=search_query)|
        Q(favourite__icontains=search_query) |
        Q(created_at__icontains=search_query)  
        )
        serializer = Contactserializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        # If no search query provided, return all contacts
        contacts = Contact.objects.all()
        serializer = Contactserializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)












#class based views

# class ContactView(APIView):
#     def get(self, request):
#         query = Contact.objects.all()
#         serializer = Contactserializer(query, many=True, context={'request':request})
#         return Response(serializer.data)
    
#     def post(self, request):
#         print(request.data)
#         serializer = Contactserializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    

#     def put(self, request, pk):
#         query = Contact.objects.get(pk=pk)
#         serializer = Contactserializer(query, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_200_OK)
        
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         query = get_object_or_404(Contact, pk=pk)
#         query.delete()
#         return Response(status.HTTP_204_NO_CONTENT)
     
# class ContactCreateView(APIView):
#     def get(self, request):
#         search_query = request.data.get('search')
#         print(search_query)
#         if search_query:
#             query = Contact.objects.filter(
#             Q(name__icontains=search_query) |  # Searching in the 'name' field
#             Q(type__icontains=search_query) |  # Searching in the 'type' field
#             Q(number__icontains=search_query)|
#             Q(favourite__icontains=search_query) |
#             Q(created_at__icontains=search_query)  
#             )
#             serializer = Contactserializer(query, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             # If no search query provided, return all contacts
#             contacts = Contact.objects.all()
#             serializer = Contactserializer(contacts, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)