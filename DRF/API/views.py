from django.shortcuts import render
from rest_framework import viewsets
from .models import*
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CompanySerializer,EmployeeSerializer
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)  # Use DRF's built-in method to get the object
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            return Response(emps_serializer.data)
        
        except Exception as e:
            return Response({
                'message':'Company Might not Exists || Error'
            }
            )
    
    
    
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer