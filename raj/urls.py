from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
import homepage.views
import products.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage.views.home, name='home'),
    path('about/', homepage.views.about, name='about'),
    path('store/', homepage.views.store, name='store'),
    path('products/whiskey/', products.views.product, name='products'),
    path('products/beer/',products.views.beer_s,name='beer'),
    path('products/wine/', products.views.wine_s, name='wine'),
    path('products/rum/', products.views.rum_s, name='rum'),
    path('products/vodka/', products.views.vodka_s, name='vodka'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


