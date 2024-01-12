import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib as mpl
from .models import *

# From news
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages



from news.models import Article, ShowImage, Tag, Category
from news.filters import ArticleFilter
from users.utils import check_group
# from users.utils import ViewCountMixin


from users.models import FavoriteArticle

# Create your views here.

# Главная страница
def index(request):

    # Old

    # dashboard = Dashboard.objects.all().first()
    # print('Автор новости', dashboard.title, ':', dashboard.author.account.gender)
    # context = {'dashboard': dashboard}

    # dashboards = Dashboard.objects.filter(author=request.user.id)
    # print(dashboards)

    # dashboards = Dashboard.objects.get(author=2)
    # print(dashboards.tags.all())

    # tag = Tag.objects.filter(title='Math').first()
    # tagged_dashboards = Dashboard.objects.filter(tags=tag)
    # print(tagged_dashboards)
    #
    # # Список всех дашбордов в разрезе пользователей
    # user_list = User.objects.all()
    # for u in user_list:
    #     print(Dashboard.objects.filter(author=u))
    # print(user_list)

    # context = {'dashboard': dashboards}

    # New

    # articles = Article.objects.all().order_by("-date")
    # p = Paginator(articles, 3)
    # page_number = request.GET.get('page')
    # page_obj = p.get_page(page_number)
    #
    # bookmarks = FavoriteArticle.objects.filter(user=request.user.id).values_list('article_id', flat=True)
    #
    # context = {'posts': page_obj, 'articles': articles, 'bookmarks': bookmarks}

    return render(request, "news/index.html")


# Страница отдельного дашборда
def mainBoard(request):
    mpl.use('agg')
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Main')
    fig = plt.gcf()
    fig.savefig('pmdash/static/pmdash/dashboards/test.png')

    context = {'dashboard': 'pmdash/static/pmdash/dashboards/test.png', }
    return render(request, "pmdash/mainBoard_page.html", context)


# Страница со списком дашбордов
def allBoards(request):
    articles = Article.objects.all().order_by("id")
    p = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    bookmarks = FavoriteArticle.objects.filter(user=request.user.id).values_list('article_id', flat=True)
    images = ShowImage.objects.all().order_by("article_id")
    context = {'posts': page_obj, 'articles': articles, 'bookmarks': bookmarks, 'images': images}
    return render(request, "pmdash/allBoards_page.html", context)


# Страница аккаунта пользователя
def account(request):

    return render(request, "pmdash/account_page.html")


# Страница контактов
def contacts(request):
    return render(request, "pmdash/contacts_page.html")


# Детализация последней записи из БД
def detail(request, id):
    dashboard = Dashboard.objects.filter(id=id).first()

    # Пример создания дашборда
    # author=User.objects.get(id=request.user.id)
    # dashboard=Dashboard(author=author, title='Заголовок1', anouncement='Анонс', text='Текст')
    # dashboard.save()

    # Пример итерирования по объектам QuerySet
    dahsboards = Dashboard.objects.all()
    s = ''
    for d in dahsboards:
        s += f'<h1>{dashboard.title}</h1><br>'

    return HttpResponse(s)


# Страница 404
def page404(request):
    return HttpResponse("404 page")
