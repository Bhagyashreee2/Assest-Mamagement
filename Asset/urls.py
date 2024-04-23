from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("modules.urls")),
    path('modules/', include('modules.urls')),
]
