from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from .models import Album, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.urls import reverse_lazy
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

def album_favorite(request, album_id):
    album = Album.objects.get(pk = album_id)
    album.is_favorite = not album.is_favorite
    album.save()
    return render(request, 'music/index.html', {'object_list': Album.objects.all()})

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'
    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #clean (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return user objects if credential are correct
            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form':form})

 # def song_favorite(request, album_id):
 #        album = get_object_or_404(Album, pk = album_id)
 #        try:
 #            selected_song = album.song_set.get(pk=request.POST['song'])
 #        except (KeyError, Song.DoesNotExist):
 #            return render(request, 'music/detail.html', {
 #                'album':album,
 #                'error_message': "You did not select a valid song",
 #            })
 #        else:
 #            selected_song.is_favorite = not selected_song.is_favorite
 #            selected_song.save()
 #            return render(request, 'music/detail.html', {'album':album})

# Create your views here.
#     def index(request):
#         all_albums = Album.objects.all()
#         context = { 'all_albums': all_albums }
#
#         #html = ''
#        # for album in all_albums:
#         #    url = '/music/' + str(album.id) + '/'
#         #   html += '<a href="' + url + '">' + album.album_title + '</a><br>'
#         return render(request, 'music/index.html', context)
#         # HttpResponse(template.render(context, request))
#
#     def detail(request, album_id):
#         #try:
#          #   album = Album.objects.get(pk=album_id)
#         #except Album.DoesNotExist:
#          #   raise Http404("Album does not exist")
#         album = get_object_or_404(Album, pk=album_id)
#         return render(request, 'music/detail.html', {'album':album})
#         #return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
#
#
