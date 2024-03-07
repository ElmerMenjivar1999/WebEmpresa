from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
from django.urls import reverse_lazy
# Create your views here.

class ProfilesListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 3

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'


    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return get_object_or_404(Profile,user__username=self.kwargs['username'])


