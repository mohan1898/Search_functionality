from django.shortcuts import render
from .models import Search
from .forms import SearchForm

def index(request):
    return render(request, 'index.html')

def search(request):
    form=SearchForm()
    results=[]
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results=Search.objects.filter(name__icontains=query)
        

    return render(request, 'search.html',{'form': form, 'results': results})