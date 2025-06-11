from tortoise import Tortoise

db = Tortoise()


async def init():
    await Tortoise.init(db_url='sqlite://db.sqlite3', modules={'models': ['db.models']})
    await Tortoise.generate_schemas()


async def on_shutdown():
    await db.close_connections()
