from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from utility.logging import Utility
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from shop_management.models import ProductDetail
from django.core.serializers import serialize
import json
utils = Utility()


class ProductDetails(APIView):
    permission_classes = (IsAuthenticated, )
    data = {'working':'yes'}

    def get(self, request):
        try:
            if request.query_params['Action']=='Filter':

                serialized_data = self.filter(request.query_params)
            else:
                product_list = ProductDetail.objects.all()
                utils.log(level='msg', msg=product_list)
                serialized_data = serialize("json", product_list)
                serialized_data = json.loads(serialized_data)
            return HttpResponse(serialized_data)
        except Exception as e:
            utils.log(level='error',msg=str(e))

    def post(self,request):
        try:
            # {'Product': [{'Name ': 'Cupcake', 'Price': 30, 'Quantity': 20, 'Stock': 100,'Id'}]}
            print(request.data)
            if request.data.get('Action')=='Add':
                for product in request.data['Product']:
                    PEntry = ProductDetail(name=product['Name'],price=product['Price'],quantity=product['Quantity'],
                                  stock=product['Stock'])
                    PEntry.save()
                    print('data inserted')
            elif request.data.get('action')=='edit':
                print('entries')
            return HttpResponse({'Data Inserted'})
        except Exception as e:
            utils.log(level='error',msg=str(e))
            return HttpResponse({'Data Insertion Failed'})

    def filter(self, filter_details):
        """
        :param filter_details: {'Action':'Filter','Field':'Name','Value':'Cupcake'}
        :return: filtered serialized data
        """
        try:
            field = filter_details['Field']
            if field == 'Name':
                product_list = ProductDetail.objects.filter(name__icontains=filter_details['Value'])
                serialized_data = serialize("json", product_list)
                serialized_data = json.loads(serialized_data)
                return serialized_data
        except Exception as e:
            utils.log(level='error',msg=str(e))