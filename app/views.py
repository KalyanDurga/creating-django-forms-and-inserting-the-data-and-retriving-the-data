from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    TFO=Topicform()
    d={'TFO':TFO}

    if request.method=='POST':
        TD=Topicform(request.POST)
        if TD.is_valid():
            topic_name=TD.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()

            TQ=Topic.objects.all()
            d1={'TQ':TQ}

            return render(request,'display_topic.html',d1)

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=Webpageform()
    d={'WFO':WFO}

    if request.method=='POST':
        WD=Webpageform(request.POST)
        if WD.is_valid():
            topic_name=WD.cleaned_data.get('topic_name')
            name=WD.cleaned_data.get('name')
            url=WD.cleaned_data.get('url')

            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
            WO.save()

            WQ=Webpage.objects.all()
            d1={'WQ':WQ}
            return render(request,'display_webpage.html',d1)

    return render(request,'insert_webpage.html',d)



def insert_accessrecod(request):
    ARO=Accessrecordform()
    d={'ARO':ARO}

    if request.method=='POST':
        AD=Accessrecordform(request.POST)
        if AD.is_valid():
            name=AD.cleaned_data['name']
            author=AD.cleaned_data['author']
            date=AD.cleaned_data['date']

            WB=Webpage.objects.get(name=name)
            AR=Accessrecord.objects.get_or_create(name=WB,author=author,date=date)[0]
            AR.save()

            ARD=Accessrecord.objects.all()
            d1={'ARD':ARD}
            return render(request,'display_accessrecord.html',d1)
        else:
            return HttpResponse('incorrect data')
    return render(request,'insert_accessrecod.html',d)



