from django.db import models
import uuid
from car_user.models import Car_User
 

class CarModel(models.Model):
    car_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    production_year = models.SmallIntegerField(null=False,blank=False)
    description = models.CharField(max_length=300,null=True)
    user = models.ForeignKey(Car_User, on_delete=models.CASCADE,related_name='car_user')

