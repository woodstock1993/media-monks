from django.contrib import admin
from django.urls import path, include

from member.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('', home),
]
