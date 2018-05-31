from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from purchase.models import Purchase
from purchase.serializer import PurchaseSerializer

class PurchaseList(generic.ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Purchase.objects.filter(purchaser=user)
