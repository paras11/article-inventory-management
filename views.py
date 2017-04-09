from django.shortcuts import render, get_object_or_404,HttpResponse
from django.shortcuts import redirect
from . models import ProductPost
from .forms import PostForm
from django.contrib.auth import(
authenticate,
get_user_model,
)
# Create your views here.
def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   posts=ProductPost.objects.all()
   return render(request,'task/post_list.html',{'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
       form = PostForm()
       return render(request, 'task/post_edit.html', {'form': form})


def price_filter_a(request):
    posts=ProductPost.objects.all().order_by('-product_price')
    return render(request, 'task/post_list.html', {'posts': posts})

def price_filter_d(request):
    posts=ProductPost.objects.all().order_by('product_price')
    return render(request, 'task/post_list.html', {'posts': posts})
def tv_filter(request):
    posts=ProductPost.objects.filter(product_type='TV')
    return render(request, 'task/post_list.html', {'posts': posts})

def ac_filter(request):
    posts=ProductPost.objects.filter(product_type='AC')
    return render(request, 'task/post_list.html', {'posts': posts})