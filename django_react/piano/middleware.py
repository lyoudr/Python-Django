import json
import jwt 
from django.http import HttpResponse

class AuthenticateMiddleWare:
  def __init__(self, get_response):
    self.get_response = get_response
  def process_view(self, request, view_func, view_args, view_kwargs):
    print('view_func is =>', view_func.__name__)
    API_KEY = 'SECRET_API_KEY'
    if view_func.__name__ == "login" or view_func.__name__ == 'FrontendAppView' or view_func.__name__ == 'upload_image':
      return None
    else:
      access_token = request.META.get('HTTP_AUTHORIZATION')
      if access_token :
        if jwt.decode(access_token, API_KEY, algorithm='HS256'):
          return None
        else:
          return HttpResponse('Token is invalid', status = 401)
      else:
        return HttpResponse('Token is invalid', status = 401)
  def __call__(self, request): 
    return self.get_response(request)
    


