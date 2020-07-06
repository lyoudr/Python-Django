from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
  path('loginpage/', views.login, name = 'login'),
  path('food/', views.food, name = 'food'),
  path('persondata/', views.persondata, name='persondata'),
  path('chat/', views.chat_records, name='chat_records'),
  path('user_image/<str:user>/', views.user_image, name='user_image'),
  path('uploadimage/<str:userId>/', views.upload_image, name='upload_image'),
  path('delete_msg/', views.delete_msg, name='delete_msg'),
  path('shortest_path/',views.shortest_path ,name='shortest_path'),
  path('shoplists/', views.GetShopItemSearchText.as_view()),
  path('shop_price/', views.GetShopItemPrice.as_view()),
  path('shop_checkout/', views.SaveShopItem.as_view()),
  path('shop_items/', views.GetShopItemsResult.as_view()),
  path('get_post/', cache_page(60*3)(views.GetUserPosts.as_view())),
  path('get_eachpost/', views.GetEachUserPost.as_view()),
  path('save_post/', views.SaveUserPost.as_view()),
  path('leave_msg/', views.LeaveMessage.as_view())
]
