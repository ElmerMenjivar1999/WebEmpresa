from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .forms import PageForm
# Create your views here.

class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del 
    staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        # if not request.user.is_staff:
        #     return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)



class PagesListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required,name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    # fields = ["title","content","order"]

    # def get_success_url(self) -> str:
    #     return reverse('pages:pages')
    
    success_url = reverse_lazy('pages:pages')

    
@method_decorator(staff_member_required,name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
   
    def get_success_url(self) -> str:
        return reverse_lazy('pages:update',args=[self.object.id]) + "?ok"


@method_decorator(staff_member_required,name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')