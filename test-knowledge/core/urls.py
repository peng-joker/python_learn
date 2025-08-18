from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/sync/wecom/', views.sync_wecom_api, name='sync_wecom_api'),
    path('api/sync/ragflow/', views.sync_ragflow_api, name='sync_ragflow_api'),
    path('api/sync/to_ragflow/', views.sync_to_ragflow_api, name='sync_to_ragflow_api'),
] 