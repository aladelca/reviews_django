from django.shortcuts import render

# Create your views here.

from .models import Review
from .forms import ReviewForm
from django.shortcuts import redirect

def index(request):
    params = {}
    return render(request, "index.html", params)

def list_review(request):
    reviews = Review.objects.all()
    params = {"reviews" : reviews}
    return render(request, "list_review.html", params)

def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})