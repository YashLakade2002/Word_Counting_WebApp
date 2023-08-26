from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            text = instance.content
            w = len(text.split())       
            count = 0
            for i in range(0, len(text)):
                if text[i] != ' ':
                    count = count + 1
            countwhite = len(text)
            instance.wspace =  count  
            instance.charcnt = countwhite
            instance.words = w              
            instance.save()
            return redirect('post-index')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'post/index.html', context)


@login_required
def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    return redirect('post-detail', pk=post.id)


@login_required
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            text = post.content
            w = len(text.split())       
            count = 0
            for i in range(0, len(text)):
                if text[i] != ' ':
                    count = count + 1
            countwhite = len(text)
            post.wspace =  count  
            post.charcnt = countwhite
            post.words = w
            form.save()
            return redirect('post-index')
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post/post_edit.html', context)


@login_required
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post-index')
    context = {
        'post': post
    }
    return render(request, 'post/post_delete.html', context)


@login_required
def counter(request):
    if request.method == 'POST':
        text = " "
        text = request.POST['texttocount']
        count = 0
        for i in range(0, len(text)):
            if text[i] != ' ':
                count = count + 1
        countwhite = len(text)
        i = False 
        if text != '':
            word = len(text.split())
            i = True
            return render(request, 'post/counter.html', 
            {
                'word': word,
                'text': text,
                'count': count,
                'countwhite': countwhite,
                'i': i,
                'on': 'active',
                })
        else:
            return render(request, 'post/counter.html', {
                'word': 0,
                'text': text,
                'count': 0,
                'countwhite': 0,
                'i': i,
                'on': 'active',
            })
    else:
        return render(request, 'post/counter.html', {
                'word': 0,
                'text': '',
                'count': 0,
                'countwhite': 0,
                'i': 'false',
                'on': 'active',
        })

