from django.shortcuts import render
from store.models import product



def home(request):
    prod=product.objects.all().filter(is_avalible=True)
    return render(request,'index.html', {'prod':prod})