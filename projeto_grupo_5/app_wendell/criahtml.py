def Cria_Html(pagina):
    import urllib.request as urllib2
    url = "https://en.wikipedia.org/wiki/"+pagina
    html = urllib2.urlopen(url).read().decode('utf-8')
    html = html.replace("//upload", "https://upload")
    html = html.replace("/w/", "https://en.wikipedia.org/w/")
    return html
#text_file = open("Output2.html", "w")
#text_file.write(isso.encode('cp850','replace').decode('cp850'))
#text_file.close()