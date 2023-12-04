from django.shortcuts import render

# Create your views here.
def example(request):
    return render(request,'steam/steam.html')
    
def example2(request):
    return render(request,'steam/aaa.html')

def example3(request):
    return render(request,'steam/bbb.html')
