from rest_framework import serializers
from .models import CRUDapi

class CRUDapiSerializer(serializers.ModelSerializer):
	class Meta:
		model = CRUDapi
		fields = '__all__'
		