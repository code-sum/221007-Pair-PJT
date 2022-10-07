from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

# Create your views here.

def main(request):
    return render(request, 'reviews/main.html')

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form,
    }
    return render(request, 'reviews/create.html', context=context)

def detail(request,pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review":review
    }
    return render(request, "reviews/detail.html", context)

def update(request, pk):
    review = Review.objects.get(pk=pk)
    review_form = ReviewForm(instance=review)
    
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:index')
    
    context ={
        "review_form": review_form
    }
    return render(request, "reviews/update.html", context)

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect("reviews:index")

    return render(request, "reviews/delete.html")
    