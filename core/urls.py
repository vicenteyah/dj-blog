from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions,routers
from blog.views import BlogViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Api for blog",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

blog_router = routers.SimpleRouter()
blog_router.register(
    r'posts', 
    BlogViewSet,
    basename='posts'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path('api-auth/', include('rest_framework.urls')),
    path("", include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
