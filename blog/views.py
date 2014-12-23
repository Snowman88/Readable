from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from .forms import PostForm, CommentForm, TagAreaForm


def post_list(request):
    posts = Post.objects.filter(created__isnull=False).order_by('created')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    # import ipdb; ipdb.set_trace()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        tags = request.POST["tags"]
        tag_area_form = TagAreaForm(initial={"tags": tags})
        # import ipdb; ipdb.set_trace()
        if form.is_valid():
            # tag
            tag_list = tags.split(",")
            # validation here
            # ex empty tag, prohibited words, etc
            # validation end
            Tag.objects.filter(post=post).delete()
            for a_tag in tag_list:
                a_tag = a_tag.strip()
                if a_tag == "":
                    continue
                tag = Tag(tag=a_tag)
                # tag.tag = a_tag
                post.tag_set.add(tag)
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        tags = post.tag_set.all().order_by('pk')  # [tagobj, ...,...]
        tag_list = ", ".join([x.tag for x in tags])
        tag_area_form = TagAreaForm(initial = {'tags': tag_list})
    return render(request, 'blog/post_edit.html', {'form': form, 'tag_area_form': tag_area_form})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')


def comment_new(request, post_id):
    # import ipdb; ipdb.set_trace()
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('blog.views.post_detail', pk=post.id)
        else:
            print("Invalid")
    return redirect('blog.views.post_detail', pk=post_id)
