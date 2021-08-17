from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import studentSerializer,studentSerializer2
from .models import studentModel

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentSerializer
    se = studentSerializer(serializer_class)
    

class UserViewSet2(APIView):
    def get(self,request):        
        queryset = studentModel.objects.values('sname','description')
        return Response(queryset)

    def post(self,request):
        d1 = request.data['sname']
        d2 = request.data['description']
        queryset = studentModel(sname=d1,description=d2)
        queryset.save()

        md = studentModel.objects.all()
        se = studentSerializer2(md,many=True)
        json_data = JSONRenderer().render(se.data)
        return HttpResponse(json_data,content_type='application/json')


class UserViewSet3(APIView):
    def get_obj(self,id):
        try:
            return studentModel.objects.get(id=id)

        except studentModel.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_obj(id=id)     
        serializer = studentSerializer2(obj)
        return Response(serializer.data)


    def put(self,request,id):
        obj = self.get_obj(id)     
        serializer = studentSerializer2(obj,data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)


    def delete(self,request,id):
        obj = self.get_obj(id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def st_details(request):
    if request.method =='GET':
        print("jkjkjk")
        md = studentModel.objects.all()
        se = studentSerializer2(md,many=True)
        json_data = JSONRenderer().render(se.data)
        return HttpResponse(json_data,content_type='application/json')


@api_view(['GET','POST','PUT','DELETE'])
def show(request,pk,*args,**kwargs):
    
    if request.method =='GET':
        # md = studentModel.objects.all()
        # se = studentSerializer2(md,many=True)
        # json_data = JSONRenderer().render(se.data)
        # return HttpResponse(json_data,content_type='application/json')
        queryset = studentModel.objects.values('sname','description')
        return Response(queryset)

    if request.method == 'POST':
        d1 = request.data['sname']
        d2 = request.data['description']
        queryset = studentModel(sname=d1,description=d2)
        queryset.save()

        md = studentModel.objects.all()
        se = studentSerializer2(md,many=True)
        json_data = JSONRenderer().render(se.data)
        return HttpResponse(json_data,content_type='application/json')


    elif request.method == 'PUT':
        # try:
        #     student = studentModel.objects.get(pk=pk)
        # except studentModel.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        # serializer = studentSerializer2(student, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        data=request.data['sname']
        queryset1=studentModel.objects.values('sname','description').filter(sname=data)	
        return Response(queryset1) 
        serializer = studentSerializer2(studentModel, data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['sname']
            desc = serializer.validated_data['description']
            serializer.save(sname=request.user,description=desc)
            # serializer.update()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



    elif request.method =='DELETE':
        try:
            queryset1=studentModel.objects.get(pk=pk)
            print(queryset1)
            queryset1.delete()
            # var1 = studentModel.objects.all()
            print("44")
            queryset = studentModel.objects.values('sname','description')
            return Response(queryset)
            # return Response(var1)       
        except studentModel.DoesNotExist: 
            return Response({'message': 'Does not exist'}, status=status.HTTP_404_NOT_FOUND)   