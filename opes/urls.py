from django.urls import path
from . import views
from django.views.i18n import set_language


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('mens/', views.mens, name='mens'),
    path('womens/', views.womens, name='womens'),
    path('kids/', views.kids, name='kids'),
    path('sport/', views.sport, name='sport'),
    path('uniform/', views.uniform, name='uniform'),
    path('bed/', views.bed, name='bed'),
    path('contact/', views.contact_view, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('cookies/', views.cookies, name='cookies'),

]