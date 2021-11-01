from rest_framework import serializers
from .models import Tractor
from .models import Attachments
from .models import Tractor_Types
from .models import Tractor_Attachments
from .models import Tractor_Sub_Types_Activities
from .models import User_Rating_Review
from . import models


class TractorSerializer(serializers.ModelSerializer):
    tractor_type = serializers.PrimaryKeyRelatedField(queryset=Tractor_Types.objects.all(),
                                                  many=False) 
    tractor_sub_type = serializers.PrimaryKeyRelatedField(queryset=Tractor_Sub_Types_Activities.objects.all(),
                                                  many=False) 

    class Meta:
        model = Tractor # this is the model that is being serialized
        fields = ('tractor_type','tractor_sub_type','owner_id','engine_power','no_of_wheels','location','is_available')
        
class TractorTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tractor_Types # this is the model that is being serialized
        fields = ('name','created')

class TractorSubtypesSerializer(serializers.ModelSerializer):
    #tractor_type_id = serializers.ReadOnlyField(source='tractor_type.uuid')
    tractor_type = serializers.PrimaryKeyRelatedField(queryset=Tractor_Types.objects.all(),
                                                  many=False) 
    
    class Meta:
        model = Tractor_Sub_Types_Activities # this is the model that is being serialized
        fields = ('tractor_type','name')


class UserRatingReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User_Rating_Review.objects.all(),
                                                  many=False)

    tractor = serializers.PrimaryKeyRelatedField(queryset=User_Rating_Review.objects.all(),
                                                  many=False)

    order = serializers.PrimaryKeyRelatedField(queryset=User_Rating_Review.objects.all(),
                                                  many=False)

    class Meta:
        model = User_Rating_Review # this is the model that is being serialized
        fields = ('user','tractor','order','rating','review')


        
        
    