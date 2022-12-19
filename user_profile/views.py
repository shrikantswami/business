from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def index(request):
    print('came here')
    print(request.body)
    if request.method == 'POST':
        print(request)
    return HttpResponse('User Created Successfully')


@csrf_exempt
def create_account(request):
    """

    :return:
    """
    try:

        return HttpResponse('User Created Successfully')
    except Exception as e:
        print(str(e))
# Create your views here.
