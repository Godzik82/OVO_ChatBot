from aiogram.filters.callback_data import CallbackData

class CardsCallBack(CallbackData, prefix="card"):

    id:str = "cards"
    category:str
    card_dict:str
    # url_photo:str
    # title:str
    # description:str


    # def __init__(self, url_record, url_photo, title, description):
    #     self.id = "cards"
    #     self.url_record = url_record
    #     self.url_photo = url_photo
    #     self.title = title
    #     self.description = description


