from datetime import datetime, timedelta
import logging
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        user = getattr(request, 'user', None)
        user_display = user if user and user.is_authenticated else 'Anonymous'
        self.logger.info(f"{datetime.now()} - User: {user_display} - Path: {request.path}")
        response = self.get_response(request)
        return response

    def process_request(self, request):
        # Log the request method and path
        print(f"Request Method: {request.method}, Request Path: {request.path}")

    def process_response(self, request, response):
        # Log the response status code
        print(f"Response Status Code: {response.status_code}")
        return response

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.now().time()
        # Restrict access outside 6PM (18:00) to 9PM (21:00)
        if not (now >= datetime.strptime("18:00", "%H:%M").time() and now <= datetime.strptime("21:00", "%H:%M").time()):
            return HttpResponseForbidden("Access to messaging app is restricted outside 6PM to 9PM.")
        return self.get_response(request)

class OffensiveLanguageMiddleware:
    message_limit = 5
    time_window = timedelta(minutes=1)
    ip_message_log = {}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only apply limit to POST requests to message endpoints
        if request.method == "POST" and "/messages" in request.path:
            ip = self.get_client_ip(request)
            now = datetime.now()

            # Clean up old entries
            self.cleanup_old_entries(ip, now)

            # Initialize log for IP if not present
            if ip not in self.ip_message_log:
                self.ip_message_log[ip] = []

            # Check limit
            if len(self.ip_message_log[ip]) >= self.message_limit:
                return HttpResponseForbidden("Message limit exceeded: Only 5 messages per minute allowed.")

            # Log this message
            self.ip_message_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def cleanup_old_entries(self, ip, now):
        if ip in self.ip_message_log:
            self.ip_message_log[ip] = [
                timestamp for timestamp in self.ip_message_log[ip]
                if now - timestamp < self.time_window
            ]

class RolepermissionMiddleware:
    """
    Middleware to enforce role-based permissions.
    Only users with role 'admin' or 'moderator' are allowed.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, 'user', None)
        # Check if user is authenticated and has the required role
        if not (user and user.is_authenticated and getattr(user, 'role', None) in ['admin', 'moderator']):
            return HttpResponseForbidden("You do not have permission to access this resource.")
        return self.get_response(request)