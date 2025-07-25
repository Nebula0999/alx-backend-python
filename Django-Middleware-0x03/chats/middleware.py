from datetime import datetime
import logging
from django.utils.deprecation import MiddlewareMixin

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