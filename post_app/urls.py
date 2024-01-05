from . import views
from django.urls import path

urlpatterns=[
    path('',views.getPosts,name='all_Posts'),
    path('detail/<int:pk>/',views.getPost,name='post_detail'),
    path("filter/<str:tagName>/", views.getPostsByTag, name="post_filter")
]