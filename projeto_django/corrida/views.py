from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import urllib.request as urllib2
def wikipage(request,objetivo,pagina):
    url = "https://en.wikipedia.org/wiki/"+pagina
    html = urllib2.urlopen(url).read().decode('utf-8')
    html = html.replace("//upload", "https://upload")
    html = html.replace("/w/", "https://en.wikipedia.org/w/")
    html = html.replace("/wiki/", "/corrida/"+objetivo+"/")
    agora = html[html.find("<title>")+7:html.find("</title>")-12]
    print("estou aqui",agora)
    print(objetivo)
    if agora.replace(" ","_") == objetivo.replace(" ","_"):
        print("ganhou")
    
    
    context = {
        "html": html
    }
    return render(request, "corrida/wikipage.htm",context)
def inicio(request):
    print("aqui")
    """
    #definindo o objetivo:
    url2 = "https://en.wikipedia.org/wiki/"+"Special:random"
    html2 = urllib2.urlopen(url2).read().decode('utf-8')
    #html = html.replace("//upload", "https://upload")
    #html = html.replace("/w/", "https://en.wikipedia.org/w/")
    #html = html.replace("/wiki/", "/corrida/"+objetivo+"/")
    objetivo = html2[html2.find("<title>")+7:html.find("</title>")-12]

    context = {
        "objetivo": objetivo
    }"""
    url2 = "https://en.wikipedia.org/wiki/"+"Special:random"
    html2 = urllib2.urlopen(url2).read().decode('utf-8')
    objetivo = html2[html2.find("<title>")+7:html2.find("</title>")-12]
    print(objetivo)
    context = {
        "objetivostr": objetivo,
        "objetivo": objetivo.replace(" ","_")
    }
    return render(request, "corrida/inicio.htm",context)