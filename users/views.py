import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import User, UserLog
from datetime import datetime

def fetch_users_from_zoho():
    url = f"https://projectsapi.zoho.com/restapi/portal/[portal_id]/users/"
    headers = {
        "Authorization": f"Zoho-oauthtoken {settings.ZOHO_ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('users', [])
    return []

def sync_users(request):
    users = fetch_users_from_zoho()

    for zoho_user in users:
        user, created = User.objects.get_or_create(
            zoho_user_id=zoho_user['id'],
            defaults={
                'name': zoho_user['name'],
                'email': zoho_user['email'],
                'status': zoho_user['status'],
                'access_type': zoho_user['role']
            }
        )

        if not created:
            user.status = zoho_user['status']
            user.access_type = zoho_user['role']
            user.save()

    return JsonResponse({"message": "Users synced successfully"}, status=200)

def update_user_status(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        new_status = request.POST.get('status')

        try:
            user = User.objects.get(zoho_user_id=user_id)
            if user.status != new_status:
                event_type = "activation" if new_status == "active" else "deactivation"
                user.status = new_status
                user.save()

                # Log the event
                UserLog.objects.create(user=user, event_type=event_type)

            return JsonResponse({"message": f"User {user.name} status updated to {new_status}"}, status=200)
        except User.DoesNotExist:
            return JsonResponse({"message": "User not found"}, status=404)
    return JsonResponse({"message": "Invalid request method"}, status=400)

def user_logs(request, user_id):
    logs = UserLog.objects.filter(user__zoho_user_id=user_id).order_by('-event_timestamp')
    log_data = [
        {"event_type": log.event_type, "timestamp": log.event_timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        for log in logs
    ]
    return JsonResponse(log_data, safe=False)
