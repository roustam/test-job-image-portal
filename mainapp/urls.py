
from django.urls import path
from .views import upload_view, images_list_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', upload_view, name = 'upload-view'),
    path('images_list', images_list_view, name = 'images_list_view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
