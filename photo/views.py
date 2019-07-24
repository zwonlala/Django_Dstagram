from django.shortcuts import render
from .models import Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required #이건 함수형 뷰에서 사용하고
from django.contrib.auth.mixins import LoginRequiredMixin #이건 클래스 형 뷰에서 사용한다

@login_required #사용시 바로 윗줄에 써주고
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})


class PhotoUploadView(LoginRequiredMixin, CreateView): #믹스인은 첫번째로 상속받는다
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id

        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})



class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

    