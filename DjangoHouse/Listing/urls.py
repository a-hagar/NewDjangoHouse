from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.Predict,name='predict'),
    path(r'^id/(?P<pk>\d+)$', views.detail, name='detail')
]
