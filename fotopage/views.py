from django.shortcuts import render
from django.views.generic import DetailView
from .models import About, Album, Lightbox, Priceofwork, Specialoffers

# Create your views here.
def index(request):
    
    Themes = Album.objects.all()
    context = {
            "Themes":Themes,
            }
    return render(request, 'fotopage/index.html', context)
def about(request):
    KSh = About.objects.values_list('aboutme', flat=True)
    if KSh:
        Ksenia_Sheen = KSh[0]
    else:
        Ksenia_Sheen = 'Это конфиденциальная информация'
    context = {
            'Ksenia_Sheen': Ksenia_Sheen}
    return render(request, 'fotopage/about.html', context)
def portfolio(request):
    queryset = Lightbox.objects.all()
    context = {
            "photos":queryset,
            }
    return render(request, 'fotopage/portfolio.html', context)
def price(request):
    price = Priceofwork.objects.all()
    context = {
            "prices":price,
            }
    return render(request, 'fotopage/price.html', context)
def specialoffer(request):
    offers = Specialoffers.objects.all()
    context = {
            "offers":offers,
            }
    return render(request, 'fotopage/specialoffer.html', context)
class AlbumDetail(DetailView):
     model = Album
     
     template_name = 'fotopage/portfolio.html'

     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['photos'] = Lightbox.objects.filter(album=self.object.id)
        
        return context