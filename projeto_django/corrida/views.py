from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Race
import urllib.request as urllib2
import random
def index(request):
    return (render(request,"corrida/index.htm"))
def wikipage(request,objetivo,pagina):
    url = "https://en.wikipedia.org/wiki/"+pagina
    html = urllib2.urlopen(url).read().decode('utf-8')
    html = html.replace("//upload", "https://upload")
    html = html.replace("/w/", "https://en.wikipedia.org/w/")
    html = html.replace("/wiki/", "/corrida/"+objetivo+"/")
    agora = html[html.find("<title>")+7:html.find("</title>")-12]
    print("estou aqui",agora)
    print(objetivo)
    ganhou = 0
    if agora.replace(" ","_") == objetivo.replace(" ","_"):
        print("ganhou")
        ganhou = 1
    
    
    context = {
        "html": html
    }
    if ganhou == 0:
        return render(request, "corrida/wikipage.htm",context)
    if ganhou == 1:
        return render(request, "corrida/fim.htm",context)
def inicio(request,modo):
    if modo == "aleatorio":
        url2 = "https://en.wikipedia.org/wiki/"+"Special:random"
        html2 = urllib2.urlopen(url2).read().decode('utf-8')
        objetivo = html2[html2.find("<title>")+7:html2.find("</title>")-12]
        largada = "Special:random"
    if modo == "normal":
        todas = Race.objects.all()
        corrida = todas[random.randint(0, len(todas)-1)]
        objetivo = corrida.end
        largada = corrida.begin
    context = {
        "objetivostr": objetivo,
        "objetivo": objetivo.replace(" ","_"),
        "largada": largada.replace(" ","_")
    }
    
    return render(request, "corrida/inicio.htm",context)
def mododejogo(request):
    return render(request, "corrida/mododejogo.htm")
