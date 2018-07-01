from django.urls import path,re_path
from .views import ForumIndexView,ForumSearchView,ForumExploreView,ForumSectionDetailView,PostCreateView,Subscribe

app_name="forum"
urlpatterns = [
    path('',ForumIndexView.as_view(),name="index"),
    path('explore/',ForumExploreView.as_view(),name="explore"),
    path('search/',ForumSearchView.as_view(),name="search"),
    re_path(r'^sections/(?P<section_link>[\w-]+)/$',ForumSectionDetailView.as_view(),name="sections"),
    path('create/', PostCreateView.as_view(), name="create"),
    path('subscribe/<int:pk>', Subscribe.as_view(), name="subscribe"),
]
