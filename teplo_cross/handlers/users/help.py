from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from db import ShopsData


class CheckOrBuyBTNs:

    @staticmethod
    async def get_cities(m_id: int):
        ikb = InlineKeyboardMarkup(inline_keyboard=[])
        check_cities = []
        for item in await ShopsData.filter().all():
            if item.city not in check_cities:
                check_cities.append(item.city)
                ikb.add(InlineKeyboardButton(text=f"🏙️ {item.city}", callback_data=f"city:{item.city}:{m_id}"))
        ikb.add(InlineKeyboardButton(text=f"Назад", callback_data=f"total_back:{m_id}"))
        return ikb

    @staticmethod
    async def get_district(city: str, m_id: int):
        ikb = InlineKeyboardMarkup(inline_keyboard=[])
        check_districts = []
        for item in await ShopsData.filter(city=city).all():
            if item.district is None:
                if item.street not in check_districts:
                    check_districts.append(item.street)
                    ikb.add(InlineKeyboardButton(text=f"🛣️ {item.street}", callback_data=f"street:{item.street}:{m_id}"))

            if item.district not in check_districts:
                check_districts.append(item.district)
                if item.district is not None:
                    ikb.add(InlineKeyboardButton(text=f"🏬 {item.district}", callback_data=f"district:{item.district}:{m_id}"))

        ikb.add(InlineKeyboardButton(text=f"Назад", callback_data=f"check_or_buy:{m_id}"))
        return ikb

    @staticmethod
    async def get_street(district: str, m_id: int):
        ikb = InlineKeyboardMarkup(inline_keyboard=[])
        check_streets = []
        city = ""
        for item in await ShopsData.filter(district=district).all():
            city = item.city
            if item.street not in check_streets:
                check_streets.append(item.street)
                if item.district is not None:
                    ikb.add(InlineKeyboardButton(text=f"🛣️ {item.street}", callback_data=f"street:{item.street}:{m_id}"))
        ikb.add(InlineKeyboardButton(text=f"Назад", callback_data=f"city:{city}:{m_id}"))
        return ikb

    @staticmethod
    async def get_links(street: str, m_id: int):
        ikb = InlineKeyboardMarkup(inline_keyboard=[])
        check_links = []
        for item in await ShopsData.filter(street=street).all():
            city = item.city
            district = item.district
            if item.link not in check_links:
                check_links.append(item.link)
                ikb.add(InlineKeyboardButton(text=f"Написать", url=item.link))
                ikb.add(InlineKeyboardButton(text=f"2ГИС", url=item.link_card_2gis))
                ikb.add(InlineKeyboardButton(text=f"ЯНДЕКС", url=item.link_card_ya))
                if item.district is None:
                    ikb.add(InlineKeyboardButton(text=f"Назад", callback_data=f"city:{city}:{m_id}"))
                if item.district is not None:
                    ikb.add(InlineKeyboardButton(text=f"Назад", callback_data=f"district:{district}:{m_id}"))
        return ikb
