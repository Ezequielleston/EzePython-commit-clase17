from django.http import HttpResponse
from django.template import Template, Context, loader


def saludar(request):
    return HttpResponse("Hola mundo!")

def segundaVista(request):
    return HttpResponse("<h1>Che! esto viene simple</h1>")

def saludo_con_nombre(request, nombre):
    return HttpResponse(f"<h1>Hola {nombre}</h1>")

#def probandoHtml(requets):
    #diccionario={"nombre":"Eze", "apellido":"Leston", "edad":19, "lista_de_notas":[1,5,6,7,8,9,2]}
    #archivo=open(r"C:\Users\ezequ\OneDrive\Escritorio\pythonproyecto1.0\proyecto1\plantillas\template1.html")
    #archivo.close()
    #template=Template(contenido)
    #contexto=Context(diccionario)
    #documento=template.render(contexto)
    #return HttpResponse(documento)


def probandoHtml(request):

    diccionario={"nombre":"Eze", "apellido":"Leston", "edad":19, "lista_de_notas":[1,5,6,7,8,9,2]}
    template=loader.get_template("template1.html")   
    documento=template.render(diccionario)
    return HttpResponse(documento)