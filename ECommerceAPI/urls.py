from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Ecommerce API",
        default_version='v1',
        description="""Documentation Of ECommerce Web App API. \nECommerce’s API platform provides many products, and resources that enable you to harness the power of ECommerce’s open, global, and real-time network.
                                This page describes what’s possible to build with the different API endpoints that are available on the platform, and how to get the access and information that you need to get started.
                                We regularly update and improve the experience and products available on the platform. These improvements make it important for you to stay informed so you don’t miss any updates.\nHere you can Signup, Login, Add, View, Update and Delete Products. In this API there's two type of User, AdminUser or NormalUser."""
    ),
    public=True,
)


urlpatterns = [
    path('api/v1/',
        include([
            path('admin/', admin.site.urls),
            path('ecom/', include('api.urls')),
            path('', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
        ])
    )
]
