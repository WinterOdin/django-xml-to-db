from .models import Searched, Package
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from .forms import InputForm


def main(request):
    form = InputForm()
    context = {
        'form': form,
    }
    return render(request, 'gathering/index.html', context)


def package_data(request):
    if request.method == 'POST':
        input_data = request.POST.copy()
        form = InputForm(input_data)

        if form.is_valid():
            form.save()
            searched = form['entry'].value()

            available_data = Package.objects.filter(
                Q(title__icontains=searched) |
                Q(link__icontains=searched) |
                Q(description__icontains=searched) |
                Q(author__icontains=searched) |
                Q(keywords__icontains=searched) |
                Q(version__icontains=searched) |
                Q(email__icontains=searched)
            ).values()

        return JsonResponse({'available_data': list(available_data)})
