from django.shortcuts import render
from describe.models import description

# Create your views here.
def index(request):
    return render(request,'index.html')

def desc(request):
    if request.method == 'POST':
        name = request.POST['name']
        text= request.POST['text']
        data = description(name=name,text=text)
        data.save()

    data=description.objects.all()
    dict = {
        'allcomment': data
    }
    return render(request,'desc.html',dict)