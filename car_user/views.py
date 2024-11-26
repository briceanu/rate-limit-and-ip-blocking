from rest_framework import viewsets, mixins ,generics
from rest_framework.decorators import APIView
from .models import Car_User
from .serializers import Car_UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth    import authenticate
from .generate_tokens import generate_tokens


class UserSignUpAPI(viewsets.GenericViewSet
                    ,mixins.CreateModelMixin,
                    mixins.ListModelMixin):
    
    queryset=Car_User.objects.all()
    serializer_class = Car_UserSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(Car_UserSerializer)
        if serializer.is_valid():
            serializer.save()
            return Response({serializer.data},status=status.HTTP_201_CREATED)
        return Response({serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class UserSingInAPI(generics.GenericAPIView):
    queryset=Car_User.objects.all()
    serializer_class = Car_UserSerializer

    def post(self,request,*args,**kwargs):
        username= request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error':'username or password not provided'},status=status.HTTP_401_UNAUTHORIZED)
                  
        user = authenticate(username=username,password=password)
        if user is None:
            return Response({'error':'username or password do not match'},status=status.HTTP_401_UNAUTHORIZED)

        tokens = generate_tokens(user)
        return Response(tokens,status=status.HTTP_200_OK)
            



                 

            
