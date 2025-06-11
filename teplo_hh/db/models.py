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
    contact_number = fields.CharField(max_length=4096)
    gender = fields.CharField(max_length=4096)
    place_of_residence = fields.CharField(max_length=4096)
    date_of_birth = fields.CharField(max_length=4096)
    minor_children = fields.CharField(max_length=4096)
    criminal = fields.CharField(max_length=4096)
    education = fields.CharField(max_length=4096)
    russian_citizenship = fields.CharField(max_length=4096)

class UserFlag(Model):
    id = fields.IntField(primary_key=True)
    tg_id = fields.IntField()
