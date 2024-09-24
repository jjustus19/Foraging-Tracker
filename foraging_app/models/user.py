from django.db.models import (Model, AutoField, CharField, IntegerField, ForeignKey,
                              CASCADE, DateField, EmailField, ImageField)


class User(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=120, null=False, unique=True)
    password = CharField(max_length=64, null=False)
    rating = IntegerField(default=0)
    badge = [("Diamond", 100000), ("Platinum", 10000), ("Gold", 1000), ("Silver", 100), ("Bronze", 10)]
    profile_image = ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=False)
    created_since = DateField(auto_now=True, null=False)


class User_Profile(Model):
    id = AutoField(primary_key=True)
    first_name = CharField(max_length=120, null=False)
    last_name = CharField(max_length=120, null=False)
    email = EmailField(max_length=254, null=False)
    home_address = CharField(max_length=254, null=False)
    phone = CharField(max_length=15, default=None)
    gender = [("Male", 2), ("Female", 1), ("Other", 9)]
    user_id= ForeignKey(User, on_delete=CASCADE)