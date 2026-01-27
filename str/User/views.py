from django.shortcuts import render
from rest_framework.response import Response
from drf_yasg.utils import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import Item
from .serializers import User_srl

# Create your views here.
class Register(APIView):
    serializers = User_srl
    @swagger_auto_schema(request_body=User_srl)
    def post(self,request):
        serializers = User_srl(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"MSG":"Succes"})
        else:
            return Response (serializers.errors)
