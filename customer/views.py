from django.shortcuts import render, redirect
from vendor.models import Kitchen, Tiffin


def index(request):
    return redirect("kitchens/")


def kitchens(request):
    kitchensList = Kitchen.objects.all()
    context = {'kitchens': kitchensList}
    return render(request, "kitchens.html", context)


def kitchen(request, kid):
    try:
        kitchenObj = Kitchen.objects.get(id=kid)

    except:
        return redirect('/')

    tiffinList = Tiffin.objects.filter(kitchen=kitchenObj)

    context = {'tiffins': tiffinList, 'kitchen': kitchenObj}

    return render(request, "tiffins.html", context)


def tiffin(request, kid, tid):
    try:
        kitchenObj = Kitchen.objects.get(id=kid)
        tiffinObj = Tiffin.objects.get(id=tid)

    except:
        return redirect('/')

    context = {'tiffin': tiffinObj, 'kitchen': kitchenObj}

    return render(request, "test.html", context)

