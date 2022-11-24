from django.shortcuts import render

# Create your views here.
def ifelse(request):
    d={'a':100,'b':200}
    return render(request,'ifelse.html',d)
