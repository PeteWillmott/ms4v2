from django.shortcuts import render
from catalogue.models import Catalogue
from news.models import News

def index(request):
    """Return the index.html file."""
    newest_picture = Catalogue.objects.exclude(sale_status=True).last()
    top_two_blogs = News.objects.all()[:2]
    context = {
        "newest_picture": newest_picture,
        "top_two_blogs": top_two_blogs
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def faq(request):
    return render(request, 'faq.html')


def how_to(request):
    return render(request, 'how-to.html')


def shipping(request):
    return render(request, 'shipping.html')

