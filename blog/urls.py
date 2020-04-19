from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('archive_space_station/',views.ArchiveSpaceStationView.as_view(),name='archive_space_station'),
    path('archive_hurricane_and_typhoon_updates/',views.ArchiveHurricaneAndTyphoonUpdatesView.as_view(),name='archive_hurricane_and_typhoon_updates'),
    path('archive_earth_day_countdown/',views.ArchiveEarthDayCountdownView.as_view(),name='archive_earth_day_countdown'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
