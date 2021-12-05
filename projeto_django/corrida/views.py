from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Race
import urllib.request as urllib2
from urllib import parse
import random
def index(request):
    return (render(request,"corrida/index.htm"))
def wikipage(request,objetivo,pagina):
    url = "https://pt.wikipedia.org/wiki/"+pagina
    scheme, netloc, path, query, fragment = parse.urlsplit(url)
    path = parse.quote(path)
    url = parse.urlunsplit((scheme, netloc, path, query, fragment))
    html = urllib2.urlopen(url).read().decode('utf-8')
    html = html.replace("//upload", "https://upload")
    html = html.replace("/w/", "https://pt.wikipedia.org/w/")
    html = html.replace("/wiki/", "/corrida/"+objetivo+"/")
    agora = html[html.find("<title>")+7:html.find("</title>")-34]
    ganhou = 0
    if agora.replace(" ","_") == objetivo.replace(" ","_"):
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
        url2 = "https://pt.wikipedia.org/wiki/"+"Especial:RandomRootpage"
        scheme, netloc, path, query, fragment = parse.urlsplit(url2)
        path = parse.quote(path)
        url2 = parse.urlunsplit((scheme, netloc, path, query, fragment))
        html2 = urllib2.urlopen(url2).read().decode('utf-8')
        objetivo = html2[html2.find("<title>")+7:html2.find("</title>")-34]
        largada = "Especial:RandomRootpage"
    if modo == "normal":
        if len(Race.objects.all())>0:
            todas = Race.objects.all()
            corrida = todas[random.randint(0, len(todas)-1)]
            objetivo = corrida.end
            largada = corrida.begin
        else:
            return render(request, "corrida/listavazia.htm")
    context = {
        "objetivostr": objetivo.replace("_"," "),
        "objetivo": objetivo.replace(" ","_"),
        "largada": largada.replace(" ","_")
    }
    
    return render(request, "corrida/inicio.htm",context)
def mododejogo(request):
    return render(request, "corrida/mododejogo.htm")
def analises(request):
    return render(request, "corrida/analises.htm")
