from rest_framework import serializers
from .models import studentModel

class studentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = studentModel
        fields = '__all__'

class studentSerializer2(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = '__all__'
        # sname = serializers.CharField(max_length = 20)
        # description = serializers.CharField(max_length = 200)

def update(self,instance,validated_data):   
    instance.sname = validated_data.get('sname',instance.sname)
    instance.description = validated_data.get('description',instance.description)     
    instance.save()
    return instance