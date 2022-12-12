from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from web.models import Task, Project

from .chetah_v1 import search as chetahV1Search

# PDF Parsin
# Prepare dataframe
#Uncomment in test, comment in prod


class MainView(TemplateView) :
    def get(self, request):
        return render(request, 'web/home.html')


class SimexView(TemplateView) :
    def get(self, request) :
        return render(request, "web/project_simex.html")#, context)

class CIO4GoodView(TemplateView) :
    def get(self, request) :
        return render(request, "web/project_cio4good.html")#, context)

class ChetahView(TemplateView) :
    template_name = "web/projects.html"

    def get(self, request):
        if request.method == 'GET':
            # Debug
            #print(request.GET)
            
            return render(request, "web/project_chetah.html")

    def post(self, request, **kwargs):
        if request.method == 'POST':
            context = {
                'search_query': "",
                'search_results': [],
            }
            query = request.POST['search-query']
            context['search_query'] = query

            context['search_results'] = chetahV1Search(query)             

            return render(request, "web/project_chetah.html", context)


def chetah_search(request, query):
    return JsonResponse({ 'search_results': chetahV1Search(query) })
