from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AdForm, RegisterForm
from .models import Ad, Category

def ad_list(request):
    query = request.GET.get("q", "")
    category_id = request.GET.get("category", "")

    ads = Ad.objects.all()

    if query:
        ads = ads.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    if category_id:
        ads = ads.filter(category_id=category_id)

    paginator = Paginator(ads, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    context = {
        "page_obj": page_obj,
        "categories": categories,
        "query": query,
        "selected_category": str(category_id),  
    }
    return render(request, "ads/ad_list.html", context)


@login_required
def ad_create(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            return redirect("ad_detail", pk=ad.pk)
    else:
        form = AdForm()
    return render(request, "ads/ad_form.html", {"form": form, "title": "Создать объявление"})


@login_required
def ad_edit(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if ad.author != request.user:
        return HttpResponseForbidden("Вы не можете редактировать чужое объявление.")

    if request.method == "POST":
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect("ad_detail", pk=ad.pk)
    else:
        form = AdForm(instance=ad)
    return render(request, "ads/ad_form.html", {"form": form, "title": "Редактировать объявление"})


@login_required
def ad_delete(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if ad.author != request.user:
        return HttpResponseForbidden("Вы не можете удалить чужое объявление.")

    if request.method == "POST":
        ad.delete()
        return redirect("ad_list")

    return render(request, "ads/ad_confirm_delete.html", {"ad": ad})


@login_required
def my_ads(request):
    ads = Ad.objects.filter(author=request.user)
    return render(request, "ads/my_ads.html", {"ads": ads})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("ad_list")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    return render(request, 'ads/ad_detail.html', {'ad': ad})

