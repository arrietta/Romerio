from django.urls import path

from Romerio import settings
from . import views
from django.conf.urls.static import static

urlpatterns = ([
                  path('', views.main, name='main'),
                  path('catalog', views.catalog, name='catalog'),
                  path('cart/', views.cart, name='cart'),
                  path('constructor/<str:key>', views.constructor, name='constructor'),
                  path('api/', views.api, name='api'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
               static(settings.STATIC_URL,document_root=settings.STATIC_ROOT))
