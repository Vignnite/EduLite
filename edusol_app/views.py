from django.shortcuts import render
from .models import Allotment1922, Cutoff1922, FinalAllotments1922, User

marks = []
n_ame = []
e_mail = []


def starting_page(request):
    return render(request, "edusol_app/index.html")


def form_cutoff(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        maths = request.POST.get('Maths')
        physics = request.POST.get('Physics')
        chemistry = request.POST.get('Chemistry')
        marks.append(tuple([str(maths), str(physics), str(chemistry)]))
        # cutof = float(maths) + float(physics)/2 + float(chemistry)/2
        u = User(name=name, email=email, maths=maths,
                 physics=physics, chemistry=chemistry)
        u.save()
        return render(request, "edusol_app/Initiate.html")
    return render(request, "edusol_app/Initiate.html")
    n_ame.append(name)
    e_mail.append(email)


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


print(n_ame, e_mail)


def second_choice(request):
    # print(marks)
    # cf = float(marks[1][1])
    cutoff = 199
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
