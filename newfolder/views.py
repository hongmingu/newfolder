from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from title.models import Title
from django.views.generic.list import ListView
from django.utils import timezone
from django.http import HttpResponse

def articles(request):
    render(request, 'artilces.html')

def search_titles(request):
    if request.method == 'POST' :
        search_text = request.POST['search_text']
    else:
        search_text = ''

    articles = Title.objects.filter(titleText__contains=search_text)

    return render(request, 'search.html', {'articles' : articles})



class AjaxListView(ListView):
    model = Title
    template_name = 'base.html'
    context_object_name = 'title_list'
    paginate_by = 2

    def get_template_names(self):
        if self.request.is_ajax():
            html = "<html><body>It is now</body></html>"
            return HttpResponse(html)


            # return ['_base.html']
        # return super(AjaxListView, self).get_template_names()
        return super(AjaxListView, self).get_template_names()

# post_list = AjaxListView.as_view(model=Title, template_name='base.html', context_object_name='title_list', paginate_by=2)
        # Create your views here.

def searched_list(request):
    query = request.GET.get("q")
    queryset_list = Title.objects.filter(titleText__contains='4')
    if request.method == 'GET':
        if request.is_ajax():
            if query:
                queryset_list = Title.objects.filter(titleText__contains='3')
                return queryset_list

    if request.method == 'POST' and 'start_manifest' in request.POST:
        queryset_list = Title.objects.filter(titleText__contains='1')

    if request.method == 'POST' and 'close_manifest' in request.POST:
        queryset_list = Title.objects.filter(titleText__contains='2')

    context = {
        'title' : queryset_list,
    }

    return render(request, 'Main.html', context)