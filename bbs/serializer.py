from rest_framework import serializers
from .models import bbs

class BbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bbs
        fields = ('id','title','content','writer','create_at','update_at')