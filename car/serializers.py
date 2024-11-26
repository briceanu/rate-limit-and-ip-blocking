from rest_framework import serializers
from .models import CarModel
from datetime import datetime  


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


    def validate_production_year(self,value):
        current_year = datetime.now().year
        if value < 1985:
            raise serializers.ValidationError(detail='Production year can not be less than 1985')
        if value > current_year:
            raise serializers.ValidationError(detail=f'Production year can be greater than {current_year}')
        return value 
