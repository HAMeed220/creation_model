from django.shortcuts import render
# Create your views here.
from app.models import *

from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

def display_topic(request):
    QLTO=Topic.objects.all()
    #QLTO=Topic.objects.all().order_by('topic_name')                  # ascending order
    #QLTO=Topic.objects.all().order_by('-topic_name')                 # descending order
    #QLTO=Topic.objects.all()
    #QLTO=Topic.objects.all().order_by(Length('topic_name'))          # length asc order
    #QLTO=Topic.objects.all().order_by(Length('topic_name').desc())   # length descending order
    #QLTO=Topic.objects.all()
    #QLTO=Topic.objects.all()[4:8:]                                   # a/c to u given range  

    d={'topic':QLTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO=WebPage.objects.all()
    #QLWO=WebPage.objects.all().order_by('name')                 # ascending order
    #QLWO=WebPage.objects.all().order_by('-name')                # descending order
    #QLWO=WebPage.objects.all()
    #QLWO=WebPage.objects.all().order_by(Length('name'))         # length asc order
    #QLWO=WebPage.objects.all().order_by(Length('name').desc())  # length descending order
    #QLWO=WebPage.objects.all()
    #QLWO=WebPage.objects.all()[3:8:]                            # a/c to u given range  
    #QLWO=WebPage.objects.all()
    
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def display_Accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'Accessrecord':QLAO}
    return render(request,'display_Accessrecord.html',d)


def insert_Topic(request):
    tn=input('enter topic Name')

    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    
    return HttpResponse('Topic data is inserted')

def insert_webpage(request):
    tn=input('enter topic name')
    n=input('enter name')
    u=input('enter url')
    g=input('enter gmail')

    To=Topic.objects.get(topic_name=tn)
    To.save()
    NWO=WebPage.objects.get_or_create(topic_name=To,name=n,url=u,gmail=g)[0]
    NWO.save()

    return HttpResponse('Webpage data is inserted')
    
def insert_access(request):
    n=input('enter the webpage name: ')
    d=input('enter date')
    a=input('enter author')

    WO=WebPage.objects.get(name=n)
    WO.save()
    NAO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    NAO.save()
    
    return HttpResponse('AccessRecord data is inserted')


    
def update_webpage(request):

    #WebPage.objects.filter(name='komram').update(topic_name='kabaddi')
    #WebPage.objects.update_or_create(topic_name='volly boll',defaults={'name':'Royal'}) it is created new line
    #WebPage.objects.filter(name='virat').update(topic_name='cricket') it is updated
    #WebPage.objects.filter(name='virat').update(topic_name='volly boll') it is updated
    #WebPage.objects.filter(name='virat').update(url='http//:virat.in')  it is updated
    CTO=Topic.objects.update_or_create(topic_name='cricket')[0]
    CTO.save()
    #WebPage.objects.update_or_create(name='Virat',defaults={'topic_name':CTO}) it is created new
    #WebPage.objects.update_or_create(topic_name='cricket',defaults={'name':'Raina'})
    #WebPage.objects.update_or_create(name='kufli',defaults={'topic_name':'Footboll'})
    WebPage.objects.filter(name='Raina',defaults={'url':'http//:suresh.in','gmail':'suresh@gmail.com'})








    QLWO=WebPage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',d)
    







