from aiogram import types, F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.callback_query import CallbackQuery
from aiogram.filters import Command, CommandStart
from card_callback import CardsCallBack

import kb
import text
from cards import *
# from get_index import get_pos

router = Router()

@router.message(CommandStart())
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu_price_category)

@router.message(Command("record"))
async def record(msg: Message):
    await msg.answer(text.record, reply_markup=kb.menu_record)

@router.message(Command("contacts"))
async def contacts(msg: Message):
    img_location = FSInputFile("location.png")
    await msg.answer_photo(img_location, caption=text.contacts)

@router.message(Command("price"))
async def price(msg: Message):
    await msg.answer(text.category, reply_markup=kb.menu_price_category)

# @router.callback_query(CardsCallBack.filter(F.id == "cards"))
# async def cards_info(clbq :CallbackQuery, clbd :dict):
#     button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", 
#         url=cards_depilation[clbd["category"]]["url_record"])]])
#     await clbq.message.answer_photo(
#         cards_depilation[clbd["category"]]["url_record"],
#         "<u><b>" + cards_depilation[clbd["category"]]["title"] + cards_depilation[["category"]]["description"],
#         reply_markup=button)

@router.callback_query(F.data == "depilation")
async def depilation(clb :CallbackQuery):
    # img_usluga = FSInputFile("complex_lite.jpg")
    await clb.message.answer("Услуги по депиляции", reply_markup=kb.menu_price_depilation)

# @router.callback_query(F.data == get_pos(F.data, cards_depilation_item))
# async def get_advice_zagar(clb :CallbackQuery):
#     print(pos)
#     pos = get_pos(F.data, cards_depilation_item)
#     button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[pos]["url_record"])]])
#     await clb.message.answer_photo(cards_depilation[pos]["url_photo"],
#                                             "<u><b>" + cards_depilation[pos]["title"] + cards_depilation[pos]["description"],
#                                             reply_markup=button)
    
@router.callback_query(F.data == cards_depilation_item[0])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[0]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[0]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[0]]["title"] + cards_depilation[cards_depilation_item[0]]["description"],
                                            reply_markup=button)

@router.callback_query(F.data == cards_depilation_item[1])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[1]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[1]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[1]]["title"] + cards_depilation[cards_depilation_item[1]]["description"],
                                            reply_markup=button)

@router.callback_query(F.data == cards_depilation_item[2])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[2]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[2]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[2]]["title"] + cards_depilation[cards_depilation_item[2]]["description"],
                                            reply_markup=button)

@router.callback_query(F.data == cards_depilation_item[3])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[3]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[3]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[3]]["title"] + cards_depilation[cards_depilation_item[3]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_depilation_item[4])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[4]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[4]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[4]]["title"] + cards_depilation[cards_depilation_item[4]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_depilation_item[5])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[5]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[5]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[5]]["title"] + cards_depilation[cards_depilation_item[5]]["description"],
                                            reply_markup=button)

@router.callback_query(F.data == cards_depilation_item[6])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[6]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[6]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[6]]["title"] + cards_depilation[cards_depilation_item[6]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_depilation_item[7])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[7]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[7]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[7]]["title"] + cards_depilation[cards_depilation_item[7]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_depilation_item[8])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[8]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[8]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[8]]["title"] + cards_depilation[cards_depilation_item[8]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_depilation_item[9])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[9]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[9]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[9]]["title"] + cards_depilation[cards_depilation_item[9]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_depilation_item[10])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[10]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[10]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[10]]["title"] + cards_depilation[cards_depilation_item[10]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_depilation_item[11])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_depilation[cards_depilation_item[11]]["url_record"])]])
    await clb.message.answer_photo(cards_depilation[cards_depilation_item[11]]["url_photo"],
                                            "<u><b>" + cards_depilation[cards_depilation_item[11]]["title"] + cards_depilation[cards_depilation_item[11]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == "cosmetology")
async def get_advice_zagar(clb :CallbackQuery):
    # img_usluga = FSInputFile("complex_lite.jpg")
    await clb.message.answer("Косметологические услуги", reply_markup=kb.menu_price_cosmetology)

@router.callback_query(F.data == cards_cosmetology_item[0])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_cosmetology[cards_cosmetology_item[0]]["url_record"])]])
    await clb.message.answer_photo(cards_cosmetology[cards_cosmetology_item[0]]["url_photo"],
                                            "<u><b>" + cards_cosmetology[cards_cosmetology_item[0]]["title"] + cards_cosmetology[cards_cosmetology_item[0]]["description"],
                                            reply_markup=button)

@router.callback_query(F.data == cards_cosmetology_item[1])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_cosmetology[cards_cosmetology_item[1]]["url_record"])]])
    await clb.message.answer_photo(cards_cosmetology[cards_cosmetology_item[1]]["url_photo"],
                                            "<u><b>" + cards_cosmetology[cards_cosmetology_item[1]]["title"] + cards_cosmetology[cards_cosmetology_item[1]]["description"],
                                            reply_markup=button)

@router.callback_query(F.data == cards_cosmetology_item[2])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_cosmetology[cards_cosmetology_item[2]]["url_record"])]])
    await clb.message.answer_photo(cards_cosmetology[cards_cosmetology_item[2]]["url_photo"],
                                            "<u><b>" + cards_cosmetology[cards_cosmetology_item[2]]["title"] + cards_cosmetology[cards_cosmetology_item[2]]["description"],
                                            reply_markup=button)    

@router.callback_query(F.data == cards_cosmetology_item[3])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_cosmetology[cards_cosmetology_item[3]]["url_record"])]])
    await clb.message.answer_photo(cards_cosmetology[cards_cosmetology_item[3]]["url_photo"],
                                            "<u><b>" + cards_cosmetology[cards_cosmetology_item[3]]["title"] + cards_cosmetology[cards_cosmetology_item[3]]["description"],
                                            reply_markup=button)

@router.callback_query(F.data == cards_cosmetology_item[4])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_cosmetology[cards_cosmetology_item[4]]["url_record"])]])
    await clb.message.answer_photo(cards_cosmetology[cards_cosmetology_item[4]]["url_photo"],
                                            "<u><b>" + cards_cosmetology[cards_cosmetology_item[4]]["title"] + cards_cosmetology[cards_cosmetology_item[4]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_cosmetology_item[5])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_cosmetology[cards_cosmetology_item[5]]["url_record"])]])
    await clb.message.answer_photo(cards_cosmetology[cards_cosmetology_item[5]]["url_photo"],
                                            "<u><b>" + cards_cosmetology[cards_cosmetology_item[5]]["title"] + cards_cosmetology[cards_cosmetology_item[5]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_cosmetology_item[6])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_cosmetology[cards_cosmetology_item[6]]["url_record"])]])
    await clb.message.answer_photo(cards_cosmetology[cards_cosmetology_item[6]]["url_photo"],
                                            "<u><b>" + cards_cosmetology[cards_cosmetology_item[6]]["title"] + cards_cosmetology[cards_cosmetology_item[6]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_cosmetology_item[7])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_cosmetology[cards_cosmetology_item[7]]["url_record"])]])
    await clb.message.answer_photo(cards_cosmetology[cards_cosmetology_item[7]]["url_photo"],
                                            "<u><b>" + cards_cosmetology[cards_cosmetology_item[7]]["title"] + cards_cosmetology[cards_cosmetology_item[7]]["description"],
                                            reply_markup=button)    

@router.callback_query(F.data == "manikur")
async def get_advice_zagar(clb :CallbackQuery):
    # img_usluga = FSInputFile("complex_lite.jpg")
    await clb.message.answer("Маникюр", reply_markup=kb.menu_price_manikur)

@router.callback_query(F.data == cards_manikur_item[0])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_manikur[cards_manikur_item[0]]["url_record"])]])
    await clb.message.answer_photo(cards_manikur[cards_manikur_item[0]]["url_photo"],
                                            "<u><b>" + cards_manikur[cards_manikur_item[0]]["title"] + cards_manikur[cards_manikur_item[0]]["description"],
                                            reply_markup=button)

@router.callback_query(F.data == cards_manikur_item[1])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_manikur[cards_manikur_item[1]]["url_record"])]])
    await clb.message.answer_photo(cards_manikur[cards_manikur_item[1]]["url_photo"],
                                            "<u><b>" + cards_manikur[cards_manikur_item[1]]["title"] + cards_manikur[cards_manikur_item[1]]["description"],
                                            reply_markup=button)

@router.callback_query(F.data == cards_manikur_item[2])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_manikur[cards_manikur_item[2]]["url_record"])]])
    await clb.message.answer_photo(cards_manikur[cards_manikur_item[2]]["url_photo"],
                                            "<u><b>" + cards_manikur[cards_manikur_item[2]]["title"] + cards_manikur[cards_manikur_item[2]]["description"],
                                            reply_markup=button)    

@router.callback_query(F.data == cards_manikur_item[3])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_manikur[cards_manikur_item[3]]["url_record"])]])
    await clb.message.answer_photo(cards_manikur[cards_manikur_item[3]]["url_photo"],
                                            "<u><b>" + cards_manikur[cards_manikur_item[3]]["title"] + cards_manikur[cards_manikur_item[3]]["description"],
                                            reply_markup=button)

@router.callback_query(F.data == cards_manikur_item[4])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_manikur[cards_manikur_item[4]]["url_record"])]])
    await clb.message.answer_photo(cards_manikur[cards_manikur_item[4]]["url_photo"],
                                            "<u><b>" + cards_manikur[cards_manikur_item[4]]["title"] + cards_manikur[cards_manikur_item[4]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_manikur_item[5])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_manikur[cards_manikur_item[5]]["url_record"])]])
    await clb.message.answer_photo(cards_manikur[cards_manikur_item[5]]["url_photo"],
                                            "<u><b>" + cards_manikur[cards_manikur_item[5]]["title"] + cards_manikur[cards_manikur_item[5]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == cards_manikur_item[6])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_manikur[cards_manikur_item[6]]["url_record"])]])
    await clb.message.answer_photo(cards_manikur[cards_manikur_item[6]]["url_photo"],
                                            "<u><b>" + cards_manikur[cards_manikur_item[6]]["title"] + cards_manikur[cards_manikur_item[6]]["description"],
                                            reply_markup=button)
    
@router.callback_query(F.data == "zagar")
async def get_advice_zagar(clb :CallbackQuery):
    # img_usluga = FSInputFile("complex_lite.jpg")
    await clb.message.answer("Маникюр", reply_markup=kb.menu_price_zagar)

@router.callback_query(F.data == cards_zagar_item[0])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_zagar[cards_zagar_item[0]]["url_record"])]])
    await clb.message.answer_photo(cards_zagar[cards_zagar_item[0]]["url_photo"],
                                            "<u><b>" + cards_zagar[cards_zagar_item[0]]["title"] + cards_zagar[cards_zagar_item[0]]["description"],
                                            reply_markup=button)

@router.callback_query(F.data == cards_zagar_item[1])
async def get_advice_zagar(clb :CallbackQuery):
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Онлайн-запись", url=cards_zagar[cards_zagar_item[1]]["url_record"])]])
    await clb.message.answer_photo(cards_zagar[cards_zagar_item[1]]["url_photo"],
                                            "<u><b>" + cards_zagar[cards_zagar_item[1]]["title"] + cards_zagar[cards_zagar_item[1]]["description"],
                                            reply_markup=button)

@router.message(F.text == "Онлайн-запись")
async def online_record(msg: Message):
    # await msg.answer('Онлайн-запись')
    await msg.connected_website('https://dikidi.online/330683')




