from django.db import models
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.sessions.models import Session

# Create your models here.
# 1. Users
class Users(models.Model):
  """
    unique key, u can use 'pk' better
  """
  username = models.CharField(max_length=255, unique=True)
  password = models.CharField(max_length=255, unique=True)
  job = models.CharField(max_length=255, default="F2E")
  hobby = models.CharField(max_length=255, default="piano")
  guide = models.CharField(max_length=255, default="Hello")
  gender = models.CharField(max_length=255, default="girl")
  country = models.CharField(max_length=255, default="Taiwan")
  position = models.CharField(max_length=255, default="/home/ann/Code/React/Photos/Ann.jpg")

  def __str__(self):
    return self.username

# 2. Chat
class Chat_Table(models.Model):
  who_send = models.ForeignKey(Users, related_name='chats', on_delete=models.CASCADE)
  who_receive = models.CharField(max_length=255)
  message = models.CharField(max_length=255)
  time = models.DateTimeField()

  def __str__(self):
    return str(self.who_send)
  
  def to_dict(self):
    """
      base_dict1
      if x: # beacuse api 1
        # update base_dict1
        return new_dict
      elif y: # for api 2
        return new2
      ....
    """
    return {
      "id": self.pk,
      "who_send": self.who_send.username,
      "who_receive": self.who_receive,
      "message": self.message,
      "time": self.time,
      "hobby": self.who_send.hobby,
      "job": self.who_send.job,
      "gender": self.who_send.gender,
      "country": self.who_send.country,
      "guide": self.who_send.guide
    }

  def dict_key(self, username):
    # return x if condition is ok otherwise y
    """
      if condition:
        return x
      else:
        return y
    """
    """
      if self.who_receive != username:
        return self.who_receive
      else:
        return self.who_send.username
    """
    return self.who_receive if self.who_receive != username else self.who_send.username

# 3. Shop
class ShopList(models.Model):
  users = models.ManyToManyField(Users, through='UserShopItem')
  item_name = models.CharField(max_length=255)
  img_src = models.CharField(max_length=255)
  description = models.CharField(max_length=1000)
  price = models.IntegerField()
  
  def rm_users(self):
    return {
      "id" : self.pk,
      "img_src": self.img_src,
      "item_name": self.item_name,
      "price": self.price,
      "description": self.description
    }
    
  def __str__(self):
    return self.item_name

class UserShopItem(models.Model):
  users = models.ForeignKey(Users, on_delete=models.CASCADE)
  shoplist = models.ForeignKey(ShopList, on_delete=models.CASCADE)
  color = models.CharField(max_length=100)
  size = models.CharField(max_length=100)

  def __str__(self):
    return self.shoplist.item_name
  
  @classmethod
  def save_to_DB(cls, shop_item, buyer):

    # find related user
    user = Users.objects.get(username = buyer)

    for item in shop_item:
      shoplist = ShopList.objects.get(item_name = item["item_name"])
      usershopitem = UserShopItem(users = user, shoplist = shoplist, color = item["color"], size = item["size"]) 
      usershopitem.save()

# 4. Discuss
class Discuss(models.Model):
  user = models.ForeignKey(Users, on_delete=models.CASCADE)
  discuss_type = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  content = models.CharField(max_length=10000)
  time = models.DateTimeField()

  def __str__(self):
    return self.title
  
  def to_data(self):
    return {
      "id": self.pk,
      "discuss_type": self.discuss_type,
      "title": self.title,
      "content": self.content,
      "time": self.time,
      "user_info": model_to_dict(self.user)
    }


class Comments(models.Model):
  user = models.ForeignKey(Users, on_delete=models.CASCADE)
  discuss = models.ForeignKey(Discuss, on_delete=models.CASCADE)
  comments = models.CharField(max_length=255)
  time = models.DateTimeField()

  def __str__(self):
    return self.comments

# class Blog(models.Model):
#     name = models.CharField("person's first name", max_length=100)
#     tagline = models.TextField()

#     def __str__(self):
#         return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     number_of_comments = models.IntegerField()
#     number_of_pingbacks = models.IntegerField()
#     rating = models.IntegerField()

#     def __str__(self):
#         return self.headline

# class Topping(models.Model):
#   name = models.CharField(max_length=100)

#   def __str__(self):
#     return self.name  

# class Pizza(models.Model):
#   toppings = models.ManyToManyField(Topping)
#   name = models.CharField(max_length=100)

#   def __str__(self):
#     return self.name  




### Model inheritance ###

### Abstract base classes
  # class CommonInfo(models.Model):
  #   name = models.CharField(max_length=100)
  #   age = models.PositiveIntegerField()
  #   class Meta:
  #     abstract = True
  #     ordering = ['name']

  # class Student(CommonInfo):
  #   home_group = models.CharField(max_length=5)
  #   class Meta(CommonInfo.Meta):
  #     db_table = 'student_info'
        # abstract will be False

  # class Student2(CommonInfo):
  #   hobby = models.CharField(max_length=100)
  #   class Meta(CommonInfo.Meta):
  #     db_table = 'student_info'
        # abstract will be False

# Multi-table inheritance 
  # class Place(models.Model):
  #   name = models.CharField(max_length=50)
  #   address = models.CharField(max_length=80)
  #   class Meta:
  #     ordering = ['name', 'address']

  # class Restaurant(Place):
  #   serves_hot_dogs = models.BooleanField(default=False)
  #   serves_pizza = models.BooleanField(default=False)
  
  # The automatically-created OneToOneField on Restaurant that links it to Place looks like this:
    # place_ptr = models.OneToOneField(
    #   Place, on_delete=models.CASCADE,
    #   parent_link=True,
    #   primary_key=True,
    # )

# Multiple inheritance
  # class Article(models.Model):
  #   article_id = models.AutoField(primary_key=True)
  #   article_name = models.CharField(max_length=255)

  # class Book(models.Model):
  #   book_id = models.AutoField(primary_key=True)
  #   book_name = models.CharField(max_length=255)

  # class BookReview(Book, Article):
  #   description = models.CharField(max_length=255)

    
  