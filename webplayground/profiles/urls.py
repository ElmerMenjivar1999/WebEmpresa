from django.urls import path
from profiles.views import ProfilesListView, ProfileDetailView

urlpatterns = [
    path("", ProfilesListView.as_view(),name='profiles_list'),
    path("<username>/", ProfileDetailView.as_view(),name='profile_detail')
]