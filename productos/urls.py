from rest_framework import routers
from .api import ProductoViewSet, PrecioViewSet  

router = routers.DefaultRouter()
router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/precios', PrecioViewSet, 'precios') 

urlpatterns = router.urls
