from tortoise.models import Model
from tortoise import fields


class Users(Model):
    id = fields.IntField(primary_key=True)
    tg_id = fields.IntField()


class TimeUsers(Model):
    id = fields.IntField(primary_key=True)
    tg_id = fields.IntField()
    time_int = fields.IntField()


class UsersData(Model):
    id = fields.IntField(primary_key=True)
    tg_id = fields.IntField()
    name = fields.CharField(max_length=4096)
    contact_phone = fields.CharField(max_length=4096)
    city_life = fields.CharField(max_length=4096)
    city_open = fields.CharField(max_length=4096)
    addition_info = fields.CharField(max_length=4096)


class UserFlag(Model):
    id = fields.IntField(primary_key=True)
    tg_id = fields.IntField()
