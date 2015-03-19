"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Language',
            'year':datetime.now().year,
        })
    )

def en(request):
    """Renders english home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/page_en.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def fr(request):
    """Renders french home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/page_fr.html',
        context_instance = RequestContext(request,
        {
            'title':"Page d'accueil",
            'year':datetime.now().year,
        })
    )

def kr(request):
    """Renders creole home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/page_kr.html',
        context_instance = RequestContext(request,
        {
            'title':'Onè'
            'year':datetime.now().year,
        })
    )	
	
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Having trouble with the app? Contact us!',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'What is MeDoc?',
            'year':datetime.now().year,
        })
    )

def medoc(request):
    """Renders the app page"""
    assert isinstance(request, HttpRequest)
    return render(
       request,
       'app/medoc.html',
       context_instance = RequestContext(request,
        {
            'title':'Medoc',
            'message':'How do you feel today?',
            'year':datetime.now().year,
        })
    )

def _head(request):
    """Renders the head page"""
    assert isinstance(request, HttpRequest)
    return render(
       request,
       'app/head.html',
       context_instance = RequestContext(request,
        {
            'title':'Head',
            'message':"Hope you'll feel better soon",
            'year':datetime.now().year,
        })
    )

