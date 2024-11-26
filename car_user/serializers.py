from rest_framework import serializers
from .models import Car_User
import re
 


class Car_UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Car_User
        fields = ['user_id','username','password','email','confirm_password']


    def validate_password(self,value):
        if not re.search(r'[A-Z]',value):
            raise serializers.ValidationError(detail='Password must contain an upper case letter.')

        if not re.search(r'\d',value):
            raise serializers.ValidationError(detail='Password must contain at least one number.')
    
        if len(value) < 6:
            raise serializers.ValidationError(detail='Password must be at least 6 characters.')
        return value
    

    def validate(self,data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Passwords do not match')

        if Car_User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('User name already exists')
        if Car_User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('Email already exists')
        return data

    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = Car_User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


