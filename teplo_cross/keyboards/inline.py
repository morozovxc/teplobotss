from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Start:
    @staticmethod
    async def start_ikb(m_id: int):
        btn1 = InlineKeyboardButton(text="🛍️ Уточнить наличие", callback_data=f"check_or_buy:{m_id}")
        btn2 = InlineKeyboardButton(text="📝 Трудоустройство", url="https://t.me/TEPLOHRBOT")
        btn3 = InlineKeyboardButton(text="💳Бонусная программа", url="https://t.me/TEPLOSTORESBOT")
        btn4 = InlineKeyboardButton(text="🤝🏼 Сотрудничество", callback_data=f"work_relation:{m_id}")
        btn5 = InlineKeyboardButton(text="🏦 Купить франшизу", callback_data=f"go_to_FRANCHISE:{m_id}")
        btn6 = InlineKeyboardButton(text="💡 Узнать соц.сети", callback_data=f"our_soc_web:{m_id}")
        ikb = InlineKeyboardMarkup(1).add(btn1, btn2, btn3, btn4, btn5, btn6)
        return ikb

class FRANCHISE:

    @staticmethod
    async def ikb(m_id: int):
        btn1 = InlineKeyboardButton(text="✍🏻Заполнить анкету", url="https://t.me/TEPLOFRANCHISEBOT")
        btn2 = InlineKeyboardButton(text="🚨Перейти на сайт", url="https://xn--80aanjeqpghmr2a9c.xn--p1ai/")
        btn3 = InlineKeyboardButton(text="Назад", callback_data=f"total_back:{m_id}")
        ikb = InlineKeyboardMarkup(1).add(btn1, btn2, btn3)
        return ikb

class OurSocWeb:

    @staticmethod
    async def ikb(m_id: int):
        btn1 = InlineKeyboardButton(text="TG", url="https://t.me/teplo_official")
        btn2 = InlineKeyboardButton(text="VK", url="https://vk.com/teplo_stores")
        btn3 = InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/@teplo_store/featured")
        btn4 = InlineKeyboardButton(text="IG", url="https://www.instagram.com/teplo_stores?igsh=YWtzdThiOXNnbWEz&utm_source=qr")
        btn5 = InlineKeyboardButton(text="Назад", callback_data=f"total_back:{m_id}")
        ikb = InlineKeyboardMarkup(1).add(btn1, btn2, btn3, btn4, btn5)
        return ikb


class WorkRelation:

    @staticmethod
    async def ikb(m_id: int):
        btn1 = InlineKeyboardButton(text="📈 Маркетинг|Реклама", callback_data=f"marketing:{m_id}")
        btn2 = InlineKeyboardButton(text="💼 Партнерство|Поставки|Оптовый заказ", callback_data=f"partnership:{m_id}")
        btn3 = InlineKeyboardButton(text="Назад", callback_data=f"total_back:{m_id}")
        ikb = InlineKeyboardMarkup(1).add(btn1, btn2, btn3)
        return ikb


class MarketingBTN:

    @staticmethod
    async def ikb(m_id: int):
        btn1 = InlineKeyboardButton(text="Написать", url="https://t.me/Akrisa")
        btn2 = InlineKeyboardButton(text="Назад", callback_data=f"work_relation:{m_id}")
        ikb = InlineKeyboardMarkup(1).add(btn1, btn2)
        return ikb

class PartnershipBTN:

    @staticmethod
    async def ikb(m_id: int):
        btn1 = InlineKeyboardButton(text="Написать", url="https://t.me/koynov13")
        btn2 = InlineKeyboardButton(text="Назад", callback_data=f"work_relation:{m_id}")
        ikb = InlineKeyboardMarkup(1).add(btn1, btn2)
        return ikb
