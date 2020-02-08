from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import translation
from django.shortcuts import redirect
from django.views.decorators.cache import cache_page

from .helpers import handle_upload_image
from .forms import UploadFileForm, ExhibitForm
from .models import Artwork2, Exhibit
from users.models import Artwork, Marker, Object

@cache_page(60 * 60)
def service_worker(request):
    return render(request, 'core/sw.js',
                  content_type='application/x-javascript')

def index(request):
    ctx = {
        "artworks": [
        ]
    }

    return render(request, 'core/exhibit.jinja2', ctx)

@cache_page(60 * 2)
def collection(request):

    exhibits = Exhibit.objects.all().order_by('-id')[:4]
    artworks = Artwork.objects.all().order_by('-id')[:8]
    markers  = Marker.objects.all().order_by('-id')[:8]
    objects  = Object.objects.all().order_by('-id')[:8]

    ctx = {
        "artworks": artworks,
        "exhibits": exhibits,
        "markers": markers,
        "objects": objects,
    }

    return render(request, 'core/collection.jinja2', ctx)

@cache_page(60 * 2)
def see_all(request):
    request_type = request.GET.get('which')
    ctx = {}    
    if   request_type == 'objects':
        ctx = { 'objects' : Object.objects.all(), }
    elif request_type == 'markers':
        ctx = { 'markers':  Marker.objects.all(), } 
    elif request_type == 'artworks':
        ctx = { 'artworks': Artwork.objects.all(), }
    elif request_type == 'exhibits':
        ctx = { 'exhibits': Exhibit.objects.all(), }

    return render(request, 'core/collection.jinja2', ctx)



def upload_image(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        image = request.FILES.get('file')
        if form.is_valid() and image:
            handle_upload_image(image)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UploadFileForm()
    return render(request, 'core/upload.jinja2', {'form': form})

def exhibit_select(request):
    if request.method == 'POST':
        form = ExhibitForm(request.POST)
        if form.is_valid():
            exhibit = form.cleaned_data.get('exhibit')
            return redirect("/" + exhibit.slug)
    else:
        form = ExhibitForm()

    return render(request, 'core/exhibit_select.jinja2', {'form':form})

def exhibit_detail(request):
    id = request.GET.get("id")
    exhibit = Exhibit.objects.get(id=id)
    ctx = {
        'exhibit':exhibit,
        'exhibitImage': "https://cdn3.iconfinder.com/data/icons/basic-mobile-part-2/512/painter-512.png",
        'artworks': exhibit.artworks.all()
    }
    return render(request, 'core/exhibit_detail.jinja2', ctx)
