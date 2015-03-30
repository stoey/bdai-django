from django.shortcuts import render

def document(request, id, name=None):
    doc = Document.objects.get(pk=id)
