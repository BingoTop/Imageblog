from django.shortcuts import render
from .models import Photo
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
'''
class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo/detail.html'
'''

@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})

class PhotoUploadView(CreateView,LoginRequiredMixin):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html'
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(DeleteView,LoginRequiredMixin):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView,LoginRequiredMixin):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'