from django.urls import path

from Romerio import settings
from . import views
from django.conf.urls.static import static

urlpatterns = ([
                   path('', views.main, name='main'),
                   path('catalog', views.catalog, name='catalog'),
                   path('cart/', views.cart, name='cart'),
                   path('privacy/', views.privacy, name='privacy'),
                   path('constructor/<str:key>', views.constructor, name='constructor'),
                   path('shpon/<str:key>', views.Shpon, name='shpon'),
                   path('api_add/', views.api_add, name='api_add'),
                   path('api_plus/', views.api_plus, name='api_plus'),
                   path('api_minus/', views.api_minus, name='api_minus'),
                   path('api_delete/', views.api_delete, name='api_minus'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
