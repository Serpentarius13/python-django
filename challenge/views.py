from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


dicti = {
    "boba": "bobin"
}


def index(request, month):
    
    strs = f"{dicti['boba']} boba"
    
    print(strs)
    
    months = list(dicti.keys())
    print(months)
    
    print(type(month))
    match month:
        case 'january':
            print('jan')
        case 'february':
            print('feb')
    return HttpResponse("This works")
