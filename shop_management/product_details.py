from django.shortcuts import render
from django.http import HttpResponse
from utility.logging import Utility
from django.views.decorators.csrf import csrf_exempt
utils = Utility()

@csrf_exempt
def get_list_of_products(request):
    try:
        print(request)
        return HttpResponse('list returned')
    except Exception as e:
        utils.log(level='error',msg=str(e))