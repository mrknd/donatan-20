from django.shortcuts import render, get_object_or_404

from stroller.models import Stroller


def catalog(request):
    strollers = Stroller.objects.all()
    context = {
        'strollers': strollers,
    }
    return render(request=request, template_name='pages/catalog.html', context=context)


def stroller_detail(request, stroller_slug=None):
    single_stroller = get_object_or_404(
        Stroller,
        slug=stroller_slug,
    )
    context = {
        'single_stroller': single_stroller,
    }
    return render(request=request, template_name='pages/stroller_detail.html', context=context)