from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import CommentForm

# Create your views here.

def getPosts(request):
    posts=Post.objects.all()
    return render(request,'postapp/list.html',context={'posts':posts})

def getPost(request,pk):
    post=Post.objects.get(pk=pk)
    comments=post.comments.all()
    tags=post.tags.all()
    print(tags)
    
    comment_form=CommentForm()
    if request.method == 'POST':
        print(request.POST)
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            parent_obj=None
            try:
                parent_id=request.POST.get('parentId')
            except:
                parent_id=None
            if parent_id:
                parent_obj=Comment.objects.get(pk=parent_id)
            if parent_obj:
                cf=comment_form.save(commit=False)
                cf.parent=parent_obj
                cf.post=post
                cf.save()
                comment_form=CommentForm()
    context={
        "post":post,
        "comment_form":comment_form,
        "comments":comments,
        'tags':tags
    }
    return render(request,'postapp/detail.html',context)


def getPostsByTag(request,tagName):
    filter=True
    postsTag=Post.objects.filter(tags__name=tagName).all()
    context={
        "postsTag":postsTag,
        'filter':filter
    }
    return render(request,'postapp/list.html',context)