from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    RegistroUsuarioView, VeiculoViewSet, LancamentoViewSet, ComparadorView,
    CatalogoViewSet, CompraViewSet,
)

router = DefaultRouter()
router.register(r'veiculos', VeiculoViewSet, basename='veiculo')
router.register(r'lancamentos', LancamentoViewSet, basename='lancamento')
router.register(r'catalogo', CatalogoViewSet, basename='catalogo')
router.register(r'compras', CompraViewSet, basename='compras')

urlpatterns = [
    path('', include(router.urls)),
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('comparador/', ComparadorView.as_view(), name='comparador'),
]