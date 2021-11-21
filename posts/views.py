from django.shortcuts import render,get_object_or_404
from .models import *



# Create your views here.


# postss = Posts.objects.filter(is_published=True,is_featured=True,category_id=e.id).order_by('-id')[:3]


def AllCatgory():
    catg = Category.objects.filter(parent=None)
    return catg


def PostsCategory(catg,nbr):
    df=[]
    for e in catg:
         posts = Posts.objects.filter(is_published=True,is_featured=False,category_id=e.id).order_by('-id')[:nbr]
         if(len(posts)!=0):          
            context1={'category':e.title,'allposts':list(posts)}
            df.append(context1)    
    return df 
           

def home(request):

    catg = AllCatgory()   

    latestpost = Posts.objects.filter(is_published=True,is_featured=True).last()

    toposts = Posts.objects.filter(is_published=True,is_featured=True).order_by('-id').exclude(id=latestpost.id)[:4]

    posts= PostsCategory(catg,3) 
                                 
    tags_list = Tag.objects.all()

    context={'catg':catg,'posts':posts,'tags_list':tags_list,'toposts':toposts,'latestpost':latestpost}

    return render(request, 'index.html', context)

def detail(request,slug):
    
    catg = AllCatgory() 
    posts= get_object_or_404(Posts, slug=slug)
    tags_list = list(posts.tag.all())
    context={'catg':catg,'posts':posts,'tags_list':tags_list}

    return render(request, 'article.html', context)


def AllPostCategory(request,slug):
    msg=''
    catg = AllCatgory() 
    cats= get_object_or_404(Category, slug=slug)
    posts = list(Posts.objects.filter(is_published=True,is_featured=False,category_id=cats.id).order_by('-id'))
    tags_list = Tag.objects.all()
    if(posts==[]):
        msg='No article for this category'    
    context={'catg':catg,'posts':posts,'tags_list':tags_list,'slug':slug,'msg':msg}

    return render(request, 'allposts.html', context)    


def AllPostTag(request,slug):
  
    catg = AllCatgory() 
    tag= get_object_or_404(Tag, slug=slug)
    posts = tag.posts_set.all()

    tags_list = Tag.objects.all()

    context={'catg':catg,'posts':posts,'tags_list':tags_list,'slug':slug}

    return render(request, 'allposts.html', context)      


def contact(request):

    catg = AllCatgory()   

    context={'catg':catg }

    return render(request, 'contact.html', context)    