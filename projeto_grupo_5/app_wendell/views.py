from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
#import criahtml
#from criahtml import Cria_Html

def detalhes(request,pagina):
    import urllib.request as urllib2
    url = "https://en.wikipedia.org/wiki/"+pagina
    html = urllib2.urlopen(url).read().decode('utf-8')
    html = html.replace("//upload", "https://upload")
    html = html.replace("/w/", "https://en.wikipedia.org/w/")
    html = html.replace("/wiki/", "/app_wendell/detalhes/")
    html = html.encode('cp850','replace').decode('cp850')
    print("alterou")
    context = {
        "html": html
    }
    return render(request, "app_wendell/detalhes.htm",context)

def se_juntar(request):
    return render(request, "app_wendell/se_juntar.htm")

def redes_sociais(request, rede):
    redes = ["instagram", "twitter", "github", "facebook"]
    links = {"instagram":"/grupo5",
            "twitter":"/grupo5", 
            "github":"/guilherme-melo/Grupo-5",
            "facebook":"/grupo5"}
    print(links[rede])
    if rede in redes:
        context ={
            "rede": rede,
            "link":links[rede]
        }
        return render(request, "app_wendell/redes.htm", context)
    else:
        return HttpResponseNotFound("Página não existe!")