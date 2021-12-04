from rest_framework import serializers

class CPFSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=5)
 