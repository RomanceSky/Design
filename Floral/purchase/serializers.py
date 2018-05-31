from rest_framework import serializers
from purchase.models import Purchase

class PurchaseSerializer(model.ModelSerializer):
    # usrname = PrimaryKeyRelatedField(many=True)
    class Meta:
        fields = ('purchaser')
