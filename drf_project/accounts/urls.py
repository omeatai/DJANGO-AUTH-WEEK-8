from .views import (RegisterAPI, LoginAPI, ChangePasswordView, ListAPIView, DetailAPIView)
from django.urls import include, path
from knox import views as knox_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
openapi.Info(
    title="DRF API",
    default_version='v1',
    description="Test description",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="contact@snippets.local"),
    license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', ListAPIView.as_view(), name='list'),
    path('<int:pk>/', DetailAPIView.as_view(), name='detail'),
    path('api/v1/register/', RegisterAPI.as_view(), name='register'),
    path('api/v1/login/', LoginAPI.as_view(), name='login'),
    path('api/v1/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/v1/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/v1/forgot_password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/v1/reset_password/', ChangePasswordView.as_view(), name='change-password'),
    
    path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
