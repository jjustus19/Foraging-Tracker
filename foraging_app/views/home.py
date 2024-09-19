from django.views import View
from django.shortcuts import render
import sitemap

class Home_View(View):
    def __init__(self):
        self.figure = sitemap.getDefaultMap()

    def get(self,request):
        return render(request, "index.html", {"map" : self.figure})