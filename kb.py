from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import text
from card_callback import CardsCallBack
from cards import *


record_buttons = [[InlineKeyboardButton(text="Онлайн-запись", url="https://dikidi.online/330683")]]
menu_record = InlineKeyboardMarkup(inline_keyboard=record_buttons)

price_category_buttons = [
    [InlineKeyboardButton(text="Депиляция", callback_data="depilation"),
    InlineKeyboardButton(text="Косметология", callback_data="cosmetology")],
    [InlineKeyboardButton(text="Маникюр", callback_data="manikur"),
    InlineKeyboardButton(text="Моментальный загар", callback_data="zagar")]
]
menu_price_category = InlineKeyboardMarkup(inline_keyboard=price_category_buttons)

price_depilation_buttons = [
    [InlineKeyboardButton(text="Глубокое бикини воск/сахар", callback_data="depilation_bikini"),
        # CardsCallBack(category = "cards_depilation", card_dict ="depilation_bikini").pack()),
        # url_photo = "f1.dikidi.net/c8/v7155/1navgg0ld8.jpg",
        # title = "Глубокое бикини воск/сахар",
        # description = "</b></u>\n\nБережная депиляция глубокого бикини. И воском, и сахаром.\n\nЦена - 1300 <s>1800р.</s>\nПродолжительность - 30 минут")
        
    InlineKeyboardButton(text="Голени/бедра воск/сахар", callback_data="depilation_bedra")],
    [InlineKeyboardButton(text="Дорожка на животе", callback_data="depilation_road_on_zhivot"),
    InlineKeyboardButton(text="Живот полностью", callback_data="full_depilation_on_zhivot")],
    [InlineKeyboardButton(text="Классическое бикини воск/сахар", callback_data="classic_bikini"),
    InlineKeyboardButton(text="Комплекс мини", callback_data="complex_mini")],
    [InlineKeyboardButton(text="Комплекс 1: глубокое бикини + подмышки + голени", callback_data="complex_1"),
    InlineKeyboardButton(text="Комплекс 2: глубокое бикини + подмышки + ноги полностью", callback_data="complex_2")],
    [InlineKeyboardButton(text="Комплекс 3: глубокое бикини+подмышки+ноги полностью+руки полностью", callback_data="complex_3"),
    InlineKeyboardButton(text="Коррекция бровей воском или сахаром по готовой форме", callback_data="correction_brow")],
    [InlineKeyboardButton(text="Лицо полностью воск/сахар", callback_data="face_off"),
    InlineKeyboardButton(text="Обучение восковая депиляция 1 день", callback_data="education_depil")]
]
menu_price_depilation = InlineKeyboardMarkup(inline_keyboard=price_depilation_buttons)

price_cosmetology_buttons = [
    [InlineKeyboardButton(text="Ноги полностью воск/сахар", callback_data="cosmetology_full_leg"),
    InlineKeyboardButton(text="Подмышечные впадины воск/сахар", callback_data="cosmetology_podmiski")],
    [InlineKeyboardButton(text="Поясница", callback_data="cosmetology_poyas"),
    InlineKeyboardButton(text="Руки до локтя воск/сахар", callback_data="cosmetology_lokot")],
    [InlineKeyboardButton(text="Удаление волос из носа", callback_data="cosmetology_nose"), 
    InlineKeyboardButton(text="Руки полностью", callback_data="cosmetology_full_arms")],
    [InlineKeyboardButton(text="Усики воск/сахар", callback_data="cosmetology_usi"),
    InlineKeyboardButton(text="Ягодицы", callback_data="cosmetology_ass")]
]
menu_price_cosmetology = InlineKeyboardMarkup(inline_keyboard=price_cosmetology_buttons)

price_manikur_buttons = [
    [InlineKeyboardButton(text="Знакомство с мастером", callback_data="manikur_intro"),
    InlineKeyboardButton(text="Коррекция ногтей", callback_data="manukur_correction")],
    [InlineKeyboardButton(text="Маникюр классический", callback_data="manikur_classic"),
    InlineKeyboardButton(text="Маникюр с покрытием гель-лак", callback_data="manikur_cover")],
    [InlineKeyboardButton(text="Модель маникюр с покрытием гель-лак", callback_data="manikur_model"), 
    InlineKeyboardButton(text="Наращивание ногтей", callback_data="manikur_add")],
    [InlineKeyboardButton(text="Ремонт одного ногтя", callback_data="manikur_service")]
]
menu_price_manikur = InlineKeyboardMarkup(inline_keyboard=price_manikur_buttons)

price_zagar_buttons = [
    [InlineKeyboardButton(text="Моментальный загар", callback_data="zagar_main"),
    InlineKeyboardButton(text="Моментальный загар (модель)", callback_data="zagar_model")]
]
menu_price_zagar = InlineKeyboardMarkup(inline_keyboard=price_zagar_buttons)

# start_menu_buttons = [
#     [InlineKeyboardButton(text="Онлайн-запись", url="https://dikidi.online/330683", callback_data="generate_text"),
#     InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image")],
#     [InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
#     InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
#     [InlineKeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
#     InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
#     [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
# ]


# menu = InlineKeyboardMarkup(inline_keyboard=start_menu_buttons)
# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

# bottom_menu_buttons = [
#     [
#     # KeyboardButton(text="Меню"),
#     KeyboardButton(text="Онлайн-запись")
#     # KeyboardButton(text="Перейти на сайт")
#     ]
# ]

# bottom_menu = ReplyKeyboardMarkup(
#     keyboard=bottom_menu_buttons,
#     resize_keyboard=True
# )