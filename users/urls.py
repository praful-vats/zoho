from django.urls import path
from .views import sync_users, update_user_status, user_logs

urlpatterns = [
    path('sync-users/', sync_users, name='sync_users'),
    path('update-user-status/', update_user_status, name='update_user_status'),
    path('user-logs/<str:user_id>/', user_logs, name='user_logs'),
]
