from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def cart(request):
    return render(request, 'cart.html')

def index(request):
    return render(request, 'index.html')

def process_language(request):
    if request.method == 'POST':
        selected_language = request.POST.get('language')
        return render(request, 'index.html')
    else:
        return HttpResponse("Invalid request method")
    
def crops(request):
    return render(request, 'crops.html')

def crops_list(request):
   
    return render(request, 'crops_list.html')