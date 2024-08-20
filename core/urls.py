from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar

urlpatterns = [
    path('secret-admin/', admin.site.urls),

    # main urls
    path('', include('library.urls')),

    path('', include('api.urls')),

    #for development
    path("__debug__/", include(debug_toolbar.urls)),
]