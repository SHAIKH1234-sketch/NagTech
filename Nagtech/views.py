from django.shortcuts import render
from technology.models import Technology
from AboutMe.models import AboutMe
def index(request):
    techlogies=Technology.objects.all().order_by('-created_date')
    about=AboutMe.objects.all()
    context={
    'techlogies':techlogies,
    'about':about,
    }
    return render(request,'index.html',context)
