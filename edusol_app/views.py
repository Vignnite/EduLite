from django.shortcuts import render


def starting_page(request):
    return render(request, "edusol_app/index.html")


def form_cutoff(request):
    return render(request, "edusol_app/Initiate.html")


def choice_detail(request):
    return render(request, "edusol_app/choice.html")
