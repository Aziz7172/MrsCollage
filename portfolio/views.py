from django.shortcuts import render
from .models import Paint
from django.shortcuts import render, get_object_or_404
from .models import Paint


def gallery(request):
    paints = Paint.objects.all()
    return render(request, 'portfolio/gallery.html', {'paints': paints})



def artwork_detail(request, pk):
    artwork = get_object_or_404(Paint, pk=pk)
    return render(request, 'portfolio/artwork_detail.html', {'artwork': artwork})