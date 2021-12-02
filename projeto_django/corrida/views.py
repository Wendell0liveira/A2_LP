from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def wikipage(request,pagina):
    import urllib.request as urllib2
    url = "https://en.wikipedia.org/wiki/"+pagina
    html = urllib2.urlopen(url).read().decode('utf-8')
    html = html.replace("//upload", "https://upload")
    html = html.replace("/w/", "https://en.wikipedia.org/w/")
    html = html.replace("/wiki/", "/corrida/wikipage/")
    html = html.encode('cp850','replace').decode('cp850')
    print("alterou")
    context = {
        "html": html
    }
    return render(request, "corrida/wikipage.htm",context)
