from .models import Searched, Package
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from .forms import InputForm


def main(request):
    form_input = InputForm()
    
    context = {
        'form_wallet':form_wallet,
    }

    return render(request, 'gathering/index.html', context)

def package_data(request):

    if request.method == 'POST':
        input_data = request.POST.copy()
        form = InputForm(input_data)

        if form.is_valid():
            form.save()
            searched = form['entry']
            available_data = Package.objects.filter(
                Q(title__icontains=searched) | 
                Q(link__icontains=searched) |
                Q(pubDate__icontains=searched) |
                Q(description__icontains=searched) |
                Q(author__icontains=searched) |
            )

        context = {
            'available_data':available_data
        }

        return JsonResponse(context)

