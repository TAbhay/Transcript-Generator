from django.urls import path

from web.views import UploadView
from web import views
urlpatterns = [
    path('', UploadView.as_view(), name="index"),
    path('upload', UploadView.as_view(), name="upload"),
    path('range-result',views.rangeResult,name='marksheet'),
    path('generate-transcript',views.generateTranscript),
]

