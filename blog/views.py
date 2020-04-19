from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Class views
class ContactView(TemplateView):
    template_name = 'blog/contact.html'


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # grab the last 4 objects from Post model, then filter based on published, ordered by published date
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
        # Find out more about '__lte' here: https://docs.djangoproject.com/en/1.10/topics/db/queries/


class ArchiveSpaceStationView(ListView):
    template_name = 'blog/archive_space_station.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now(), post_type='space_station').order_by('-published_date')


class ArchiveHurricaneAndTyphoonUpdatesView(ListView):
    template_name = 'blog/archive_hurricane_and_typhoon_updates.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now(), post_type='hurricane_and_typhoon_updates').order_by('-published_date')


class ArchiveEarthDayCountdownView(ListView):
    template_name = 'blog/archive_earth_day_countdown.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now(), post_type='earth_day_countdown').order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'  # go to login if they're not logged in
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


# YTF template wrongly referring to Post_list
class DraftListView(LoginRequiredMixin,ListView):
    # template_name = 'blog/post_draft_list.html'
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


# Function views
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk  # save the comment before deleting it because otherwise the return line won't know what to return
    comment.delete()
    return redirect('post_detail', pk=post_pk)
