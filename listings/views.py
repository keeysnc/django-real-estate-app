from django.shortcuts import render

# create a function to return the rendered listing url that was requested


def index(request):
    return render(request, 'listings/listings.html')


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
