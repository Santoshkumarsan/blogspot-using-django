from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import CommentForm,ContactusForm
from taggit.models import Tag
from django.db.models import Q

# Create your views here.
def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    paginator=Paginator( post_list,5)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)


    return render(request,'blogapp/post_list.html',{'post_list':post_list,'tag':tag})


def post_detail_view(request,year,month,day,post):

    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()

    return render(request,'blogapp/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})


def search(request):
    query=request.GET['query']
    allpost=Post.objects.filter(Q(body__icontains=query)|Q(title__icontains=query)|Q(category__icontains=query)|Q(created__icontains=query))
    return render(request,'blogapp/searchfunc.html',{'allpost':allpost})

def Contact_us_view(request):
    if request.method == 'POST':
        form =ContactusForm(request.POST)
        if form.is_valid():
            form.save()
            # send email code goes here
            return render(request,'blogapp/post_list.html',{'form': form})
    else:
        form =ContactusForm()

    return render(request, 'blogapp/contactUs.html', {'form': form})



def Sports(request):

    sports=Post.objects.filter(category__contains='sports' or 'game')
    #sports=Post.objects.filter(body__icontains=sport)


    paginator=Paginator( sports,4)
    page_number=request.GET.get('page')
    try:
        sports=paginator.page(page_number)
    except PageNotAnInteger:
        sports=paginator.page(1)
    except EmptyPage:
        sports=paginator.page(paginator.num_pages)

    return render(request,'blogapp/sports.html',{'sports':sports})


def Movie(request):

    movies=Post.objects.filter(category__contains='movie' or 'bollywood')
    #sports=Post.objects.filter(body__icontains=sport)


    paginator=Paginator( movies,4)
    page_number=request.GET.get('page')
    try:
        movies=paginator.page(page_number)
    except PageNotAnInteger:
        movies=paginator.page(1)
    except EmptyPage:
        movies=paginator.page(paginator.num_pages)

    return render(request,'blogapp/movies.html',{'movies':movies})

def Education_view(request):

    Education=Post.objects.filter(category__contains='education' or 'knowledge')
    #sports=Post.objects.filter(body__icontains=sport)


    paginator=Paginator( Education,4)
    page_number=request.GET.get('page')
    try:
        Education=paginator.page(page_number)
    except PageNotAnInteger:
        Education=paginator.page(1)
    except EmptyPage:
        Education=paginator.page(paginator.num_pages)

    return render(request,'blogapp/education.html',{'Education':Education})

def Star_view(request):

    star=Post.objects.filter(category__contains='star' or 'cricket' or 'bollywood' or 'hollywood'or'ollywood'or 'tollywood')
    #sports=Post.objects.filter(body__icontains=sport)


    paginator=Paginator(star,4)
    page_number=request.GET.get('page')
    try:
        star=paginator.page(page_number)
    except PageNotAnInteger:
        star=paginator.page(1)
    except EmptyPage:
        star=paginator.page(paginator.num_pages)

    return render(request,'blogapp/star.html',{'star':star})

def World_view(request):

    world=Post.objects.filter(category__contains='world' or 'world news' or 'international'or 'foreign')
    #sports=Post.objects.filter(body__icontains=sport)


    paginator=Paginator(world,4)
    page_number=request.GET.get('page')
    try:
        world=paginator.page(page_number)
    except PageNotAnInteger:
        world=paginator.page(1)
    except EmptyPage:
        world=paginator.page(paginator.num_pages)

    return render(request,'blogapp/worldnews.html',{'world':world})

def Travel_view(request):

    travel=Post.objects.filter(category__contains='travel' or 'visit')
    #sports=Post.objects.filter(body__icontains=sport)


    paginator=Paginator(travel,4)
    page_number=request.GET.get('page')
    try:
        travel=paginator.page(page_number)
    except PageNotAnInteger:
        travel=paginator.page(1)
    except EmptyPage:
        travel=paginator.page(paginator.num_pages)

    return render(request,'blogapp/travel.html',{'travel':travel})

def Cricket_view(request):

    cricket=Post.objects.filter(category__contains='cricket')
    #sports=Post.objects.filter(body__icontains=sport)


    paginator=Paginator(cricket,4)
    page_number=request.GET.get('page')
    try:
        cricket=paginator.page(page_number)
    except PageNotAnInteger:
        cricket=paginator.page(1)
    except EmptyPage:
        cricket=paginator.page(paginator.num_pages)

    return render(request,'blogapp/cricket.html',{'cricket':cricket})
