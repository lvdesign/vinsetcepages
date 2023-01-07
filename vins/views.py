from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin  # new
from django.shortcuts import render, redirect, get_object_or_404  # mail
from django.views.generic.edit import DeleteView
from vins.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.urls import reverse_lazy, reverse
# Search
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.humanize.templatetags.humanize import naturaltime


from vins.models import Vin, Comment, Fav, Category, Tag, Producteur
from vins.forms import CommentForm, VinForm
from vinsetcepages.utils import dump_queries
# Test query


# VIN
class VinListView(OwnerListView):
    ''' Vins : liste, visible par tous'''
    model = Vin
    template_name = 'vin_list.html'

    def get(self, request):
        strval = request.GET.get("search", False)
        # SEARCH name = search
        # vin_list = Vin.objects.all()
        # print(vin_list)

        if strval:
            query = Q(title__contains=strval)
            query.add(Q(description__contains=strval), Q.OR)
            vin_list = Vin.objects.filter(query).select_related().order_by('-updated')[:10]
        else:
            vin_list = Vin.objects.all().order_by('-updated')[:10]

        for obj in vin_list:
            obj.natural_updated = naturaltime(obj.updated)[:10]

        #  FAV
        favorites = list()
        if request.user.is_authenticated:
            rows = request.user.favorite_vins.values('id')
            favorites = [row['id'] for row in rows]
        print(favorites)

        ctx = {'vin_list': vin_list, 'search': strval, 'favorites': favorites}
        #  dump_queries()

        retval = render(request, self.template_name, ctx)
        return retval


class VinDetailView(OwnerDetailView): # new
    ''' Vins : detail visible par tous'''
    model = Vin
    template_name = 'vin_detail.html'

    ''' Comment '''
    def get(self, request, slug=None) :
        x = Vin.objects.get(slug=slug)
        print('x :::', x)
        comments = Comment.objects.filter(vin=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'vin' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

'''
CRUD section des vins
LoginRequiredMixin pour Creta, Update, Delete
UserPassesTestMixin pour limiter user to Update et Delete
'''

class VinCreateView(OwnerCreateView): 
    ''' Creer/editer vins: 
    'title','slug','description','price','boutique','tips','image','category','tag','score', producteur    
    model = Vin
    template_name = 'vin_new.html'   
    fields = 'title','slug','description','price','boutique','tips','image','category','tag','score', 'producteur' #'__all__'  
    success_url = reverse_lazy('vins:vin_list')
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
    '''

    model = Vin
    template_name = 'vin_new.html'
    success_url = reverse_lazy('vins:vin_list')

    def get(self, request, pk=None):
        form = VinForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = VinForm(request.POST, request.FILES or None)
        # ajouter d'abord les tags ??
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        
        # Add owner to the model before saving
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        # save m2m
        form.save_m2m() 
        dump_queries()
        return redirect(self.success_url)


class VinUpdateView(OwnerUpdateView): # new
    ''' Update vins
    model = Vin
    fields = 'title','slug','description','price',
    'boutique','tips','image','category','tag','score', 'producteur',
    template_name = 'vin_edit.html'
    success_url = reverse_lazy('vins:vin_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user
    '''
    model = Vin
    template_name = 'vin_edit.html'
    success_url = reverse_lazy('vins:vin_list')

    def get(self, request, pk):
        post_vin = get_object_or_404(Vin, id=pk,  author=self.request.user)
        form = VinForm(instance=post_vin)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    # , slug=None  id=pk, slug=pk,
    def post(self, request, pk=None):
        post_vin = get_object_or_404(Vin, id=pk, author=self.request.user)
        form = VinForm(request.POST, request.FILES or None, instance=post_vin)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        post_vin = form.save(commit=False)
        post_vin.save()
        dump_queries()
        return redirect(self.success_url)



class VinDeleteView(OwnerDeleteView): # new
    ''' Delete vins '''
    model = Vin
    template_name = 'vin_delete.html'
    success_url = reverse_lazy('vins:vin_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


def stream_file(request, pk) :
    pic = get_object_or_404(Vin, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.image)
    response.write(pic.image)
    return response


# Producteur
class ProducteurListView(OwnerListView):
    ''' Producteurliste '''
    model = Producteur
    context_object_name = 'producteur_list'
    template_name = "producteur_list.html"

    def get_queryset(self):
        context_data = Producteur.objects.all()
        return context_data


# Category -> region
class CategoryListView(OwnerListView):
    ''' Category/Region liste '''
    model = Category
    context_object_name = 'category_list'
    template_name = "category_list.html"

    def get_queryset(self):
        context_data = Category.objects.all()
        return context_data


class CategoryDetailView(OwnerDetailView):
    ''' Category/Region details '''
    model = Category
    template_name = "category_detail.html"

    def get_context_data(self, **kwargs):

        toto = Category.objects.all()
        titi = Category.objects.filter().values('name')

        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['image'] = toto
        context['test'] = titi
        return context

    def get_queryset(self):
        return Category.objects.all()


# Tag -> Cepages
class TagListView(OwnerListView):
    ''' Tag/Cepage liste '''
    model = Tag
    context_object_name = 'tag_list'
    template_name = "tag_list.html"

    def get_queryset(self):
        return Tag.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagsall'] = Tag.objects.all()

        return context


class TagDetailView(OwnerDetailView):
    ''' Tag/Cepage detail '''
    model = Tag
    template_name = "tag_detail.html"

    def get_queryset(self):
        return Tag.objects.all()


# COMMENTS
class CommentCreateView(LoginRequiredMixin, View):

    def post(self, request, slug=None):
        f = get_object_or_404(Vin, slug=slug)
        print('f :::',f)
        comment = Comment(text=request.POST['comment'], author=request.user, vin=f)
        comment.save()
        return redirect(reverse('vins:vin_detail', args=[slug]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "vin_comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        vin = self.object.vin
        return reverse('vins:vin_detail', args=[vin.slug])
        #return reverse_lazy( 'vins:vin_detail', kwargs={'vin.slug': vin.slug })





from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError


@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    ''' Favoris Vin / User '''
    def post(self, request, pk):
        print("Vin PK", pk)
        t = get_object_or_404(Vin, id=pk)
        fav = Fav(user=request.user, vin=t)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK",pk)
        t = get_object_or_404(Vin, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, vin=t).delete()
        except Fav.DoesNotExist as e:
            pass

        return HttpResponse()


"""Service worker for offline app"""
class ServiceWorker(View):
    template_name = "vins/sw.js"
    content_type = "application/javascript"
