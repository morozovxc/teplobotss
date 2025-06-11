from tortoise.models import Model
from tortoise import fields


class ShopsData(Model):
    id = fields.IntField(primary_key=True)
    city = fields.CharField(max_length=255)
    district = fields.CharField(max_length=255, null=True)
    street = fields.CharField(max_length=255)
    link = fields.CharField(max_length=255)
    link_card_ya = fields.CharField(max_length=555)
    link_card_2gis = fields.CharField(max_length=555)


class Users(Model):
    id = fields.IntField(primary_key=True)
    tg_id = fields.IntField()