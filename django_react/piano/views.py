import jwt
import json
import time
import os.path
from datetime import datetime
from . import algorithm
from .models import Users, Chat_Table, ShopList, UserShopItem, Discuss, Comments
from datetime import datetime, timedelta
from django.db.models import Q
from django.shortcuts import render
from django.core import serializers
from django.views import View
from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.views.decorators.http import require_GET, require_POST
from django.core.files.storage import FileSystemStorage
from django.forms.models import model_to_dict
from django.db.models import Count
from django.core import serializers
from django.db import transaction, connection
from django.core.cache import caches
from django.views.decorators.cache import cache_page
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.utils.timezone import utc


cache = caches['default']

class QueryLogger:
  def __init__(self):
    self.queries = []

  def __call__(self, execute, sql, params, many, context):
    current_query = {'sql': sql, 'params': params, 'many': many}
    start = time.monotonic()
    try:
      result = execute(sql, params, many, context)
    except Exception as e:
      current_query['status'] = 'error'
      current_query['exception'] = e
      raise
    else:
      current_query['status'] = 'ok'
      return result
    finally:
      duration = time.monotonic() - start
      current_query['duration'] = duration
      self.queries.append(current_query)


### Login ###
# 1. Login to get access token #OK
# @require_POST
def login(request):
  user_info = json.loads(request.body)
  username = user_info['userId']
  password = user_info['password']
  API_KEY = 'SECRET_API_KEY'
 
  # Verify if user info is right
  is_user = Users.objects.filter(username=username).filter(password=password)
  
  if len(is_user) != 0:    
    payload = {
      "username": username,
      "password": password,
      "exp": datetime.utcnow() + timedelta(hours=9)
    }
    access_token = jwt.encode(payload, API_KEY, algorithm='HS256').decode("utf8")
    resp = JsonResponse({'status': 'OK', 'token': access_token, 'userId': username}, status = 200)
    # Verify if session existed, if it is esisted, return OK
    s_set = Session.objects.all()
    for s in s_set : 
      if s.expire_date > datetime.utcnow().replace(tzinfo=utc) and str(is_user[0].id) == s.get_decoded().get('userId'):
        return resp
    # Create New Session
    request.session['userId'] = str(is_user[0].id)
    request.session.set_expiry(30000)
    return JsonResponse({
      'status': 'OK',
      'token': access_token,
      'userId': username
    }, status = 200)
  elif len(is_user) == 0:
    return HttpResponse('Permission denied', status=401)
  
# 2. Select food to get dishes #OK
def food(request):
  input_food = json.loads(request.body)
  print('input_food is =>', input_food)
  returneddishes = algorithm.countDishes(input_food)
  # cache.set('returnddishes', returneddishes)
  resp = JsonResponse({
    'message': 'ok',
    'dishes': returneddishes
  }, status = 200)
  return resp
### Chat ###
# 1. Post personal image to backend
def upload_image(request, userId):
  # print('request.FILES name is =>', request.FILES)
  # if request.method == 'POST':
  #   user_file = request.FILES["photo"]
  #   fs = FileSystemStorage()
  #   fs.save(user_file.name, user_file)
  #   if os.path.isfile('/home/ann/Code/GitLab/React/Photos/' + user_file.name):
  #     return JsonResponse({'status': 'ok'})
  #   else:
  #     return HttpResponseBadRequest()
  return JsonResponse({'status': 'ok'})

# 2. Save personal data to Mysql DataBase #OK
@transaction.atomic
def persondata(request):
  # This code executes inside a transaction.
  user_info = json.loads(request.body)
  print('user_info is =>', user_info)
  userId = user_info["userId"]
  country = user_info["country"]
  gender = user_info["gender"]
  guide = user_info["guide"]
  hobby = user_info["hobby"]
  job = user_info["job"]
  if Users.objects.filter(username=userId):
    Users.objects.filter(username=userId).update(country=country, gender=gender, guide=guide, hobby=hobby, job=job)
    if Users.objects.filter(username=userId, country=country, gender=gender, guide=guide, hobby=hobby, job=job).exists():
      return HttpResponse('Update success', status = 200)
    else :
      raise ObjectDoesNotExist
  else :
    raise ObjectDoesNotExist

# 3. Query chat records
@transaction.atomic
@cache_page(600, cache='default', key_prefix='') # represent each response of this view will becached for 15 min.
def chat_records(request):
  q_person = request.GET["personId"]
  user = Users.objects.get(username=q_person)
  """
    Normal query:
      1. .filter(id__contains=[1,2,3,4,5], username='hello', money__gre=100,...)
    Q complex Query:
    complexQ = Q(Q(C1) || Q(C2) && Q(C3)...)
    m.objects.filter(complexQ)
  """
  chats_records = Chat_Table.objects.filter(Q(who_send=user) | Q(who_receive=user.username)) # explain what is Q?
  resp = {}

  for r in chats_records:
    try:
      with transaction.atomic():
        transaction.on_commit(lambda : print('transaction sucess!'))
        resp[r.dict_key(user.username)].append(r.to_dict())
    except KeyError:
      resp[r.dict_key(user.username)] = [r.to_dict()]

  return JsonResponse(resp, status=200)


# 4. Get User Images
def user_image(request, user):
  try:
    target_user = Users.objects.get(username=user)
    img_res = FileResponse(open(target_user.position, 'rb'))
    return img_res
  except:
    return HttpResponseNotFound("File Not Found")

# 5. Delete message
def delete_msg(request):
  del_info = json.loads(request.body)
  delete_item = Chat_Table.objects.filter(who_receive = del_info["who_receive"], message = del_info["message"], who_send_id = del_info["who_send_id"])
  delete_item.delete()
  if len(delete_item) == 0:
    return JsonResponse({'status': 'ok', 'isDeleted': 'yes'}, status = 200)
  else:
    return HttpResponse('delete failed', status = 403)

### Courses ###
# 1. Post path to count shortest path
@require_POST
def shortest_path(request):
  points = json.loads(request.body)
  path = algorithm.count_path(points[0][5], points[1][5])
  return JsonResponse({'path': path}, status=200)

### ShopList ###
# 1. Get shop list according to search text
class GetShopItemSearchText(View):
  def post(self, request):
    text = json.loads(request.body)['searchText']
    founded_items = ShopList.objects.filter(Q(item_name__contains=text))
    data = [item.rm_users() for item in founded_items]
    resp = {'data' : data}
    return JsonResponse(resp, safe=False, status=200)

# 2. Get shop items according to price
class GetShopItemPrice(View):
  def post(self, request):
    data = json.loads(request.body)
    min_price = [num.strip() for num in data["price"].split("~")][0]
    max_price = [num.strip() for num in data["price"].split("~")][1]
    founded_items = ShopList.objects.filter(price__lte=max_price, price__gte=min_price)
    resp = [item.rm_users() for item in founded_items]
    return JsonResponse(resp, safe=False, status=200)

# 3. Save user shop items to DB
class SaveShopItem(View):
  def post(self, request):
    # define buyer and user post shop_item
    buyer = json.loads(request.body)['buyer']
    shop_item = json.loads(request.body)['shop_item']
    
    # number in shopitems before adding
    number_before = UserShopItem.objects.all().count() # item number before adding

    UserShopItem.save_to_DB(shop_item, buyer)

    # number in shopitems after adding
    number_after = UserShopItem.objects.all().count() # item number after adding

    if number_after == number_before + len(shop_item) :
      return JsonResponse({'issavetoDB': 'yes', 'status': 'ok'})
    else :
      raise HttpResponse('save error', status = 400)

# 4. Get user shop items, user info from DB
class GetShopItemsResult(View):
  def get(self, request, *args, **kwargs):
    user = request.GET["user"]
    ql = QueryLogger()
    # Get query efficacy
    with connection.execute_wrapper(ql):
      found_user = Users.objects.get(username=user)
      ar_shopitems = found_user.shoplist_set.all().values().annotate(total = Count('item_name')).order_by('total')
      dict_ar = [item for item in ar_shopitems]
      result = {
        'user_info': model_to_dict(found_user),
        'shop_items': dict_ar
      }
    print(ql.queries)
    return JsonResponse(result, status=200)  

### Discuss ###
# 1. Get posts
class GetUserPosts(View):
  def get(self, request):
    discuss_type = request.GET["discuss_type"]
    posts = Discuss.objects.filter(discuss_type = discuss_type).order_by('time')
    dict_posts = [post.to_data() for post in posts]
    return JsonResponse(dict_posts, safe = False ,status = 200)

# 2. Get Each Post
class GetEachUserPost(View):
  def get(self, request):
    post_id = request.GET["post_id"]
    discuss_post = Discuss.objects.get(id = post_id)
    comments = [model_to_dict(comment) for comment in discuss_post.comments_set.all()]
    resp = {
      'discuss' : model_to_dict(discuss_post),
      'comments' : comments
    }
    return JsonResponse(resp, safe = False ,status = 200)

# 3. Save post
class SaveUserPost(View):
  def post(self, request):
    save_info = json.loads(request.body)
    try:
      post = Discuss(discuss_type = save_info["discuss_type"], title = save_info["title"], content = save_info["content"], time = save_info["time"], user_id = save_info["user_id"])
      post.save()
    except Exception as error:
      print('error is =>', error)
    return JsonResponse({'status': 'ok', 'isSaved': True})

# 4. Leave a message
class LeaveMessage(View):
  def post(self, request):
    msg_info = json.loads(request.body)
    try:
      comment = Comments(comments = msg_info["comment"], time = msg_info["time"],  discuss_id = msg_info["discuss_id"], user_id = msg_info["user_id"])
      comment.save()
    except Exception as error:
      print('error is =>', error)
    return JsonResponse({'status': 'ok', 'isLeaveMsg': True})
  