from django.shortcuts import render
from .models import Allotment1922, Cutoff1922, FinalAllotments1922, Users
from django.http import HttpResponseRedirect

marks = []
n_ame = []
e_mail = []
cuts = []


def starting_page(request):
    return render(request, "edusol_app/index.html")


def form_cutoff(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        maths = request.POST.get('Maths')
        physics = request.POST.get('Physics')
        chemistry = request.POST.get('Chemistry')
        mat = float(maths)
        phy = float(physics)
        chem = float(chemistry)
        marks.clear()
        marks.append(tuple([str(maths), str(physics), str(chemistry)]))
        cutof = mat + phy/2 + chem/2
        cuts.clear()
        cuts.append(cutof)
        u = Users(name=name, email=email, maths=mat,
                  physics=phy, chemistry=chem)
        u.save()
        n_ame.append(name)
        e_mail.append(email)
        # print("the cutoof is", cutof)
        # print(marks)
        # print(n_ame, e_mail)
        return HttpResponseRedirect("/Choices")
    return render(request, "edusol_app/Initiate.html")


def choice_detail(request):
    return render(request, "edusol_app/choice.html")

# def second_choice(request):
#     cutoff = 199.5
#     allotment_table = Allotment1922.objects.all()
#     return render(request, "edusol_app/choice02.html", locals())

# def second_choice(request):
#     cutoff = 199.5
#     allotment_table = Allotment1922.objects.filter(cutoff__gt=cutoff).values()
#     return render(request, "edusol_app/choice02.html", locals())


def second_choice(request):
    # print(marks)
    # cf = float(marks[1][1])
    print("the cut from form page is : ", *cuts, *marks)
    cutoff = cuts[0]
    # module = User.objects.get(name=n_ame[0], email=e_mail[0])
    # print(module)
    # allotment_table_header = [
    #     f.name for f in Allotment1922._meta.get_fields('collegename', 'cutoff')]
    allotment_table = [list(i.values())
                       for i in list(FinalAllotments1922.objects.filter(meancutoff__lte=cutoff).order_by('-meancutoff').values('collegecode', 'collegename', 'community', 'meancutoff', 'branchcode', 'branchname'))]
    choices_count = len(allotment_table)
    return render(request, "edusol_app/choice02.html", {
        # "allotment_table_header": allotment_table_header,
        "choices_count": choices_count,
        "allotment_table": allotment_table,
        "cf": cutoff
    })


def second_choice1(request):
    # print(marks)
    # cf = float(marks[1][1])
    print("the cut from form page is : ", *cuts, *marks)
    cutoff = cuts[0]
    # module = User.objects.get(name=n_ame[0], email=e_mail[0])
    # print(module)
    # allotment_table_header = [
    #     f.name for f in Allotment1922._meta.get_fields('collegename', 'cutoff')]
    allotment_table = [list(i.values())
                       for i in list(FinalAllotments1922.objects.filter(meancutoff__gte=cutoff).order_by('-meancutoff').values('collegecode', 'collegename', 'community', 'meancutoff', 'branchcode', 'branchname'))]
    choices_count = len(allotment_table)
    return render(request, "edusol_app/choice02.html", {
        # "allotment_table_header": allotment_table_header,
        "choices_count": choices_count,
        "allotment_table": allotment_table,
        "cf": cutoff
    })
