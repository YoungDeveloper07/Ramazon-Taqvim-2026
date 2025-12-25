from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


menu_buttons = [
    [
        KeyboardButton(text="Taqvim"),
        KeyboardButton(text="Ilm maskani")
    ],
    [
        KeyboardButton(text="Bot Haqida")
    ]
]

main_menu = ReplyKeyboardMarkup(
    keyboard=menu_buttons,
    resize_keyboard=True, 
    one_time_keyboard=False 
)

#-----Namoz Vaqrlari uchun ------------------------------------------------------------------------
namoz_buttons = [
    [
        InlineKeyboardButton(text = 'Toshkent', callback_data='toshkent'),
        InlineKeyboardButton(text = 'Namangan', callback_data='namangan'),
        InlineKeyboardButton(text = 'Andijon', callback_data='andijon')
        
    ],
    [
        InlineKeyboardButton(text = 'Farg\'ona', callback_data='fagona'),
        InlineKeyboardButton(text = 'Sirdaryo', callback_data='sirdaryo'),
        InlineKeyboardButton(text = 'Jizzax', callback_data='jizzax')
        
    ],
    [
        InlineKeyboardButton(text = 'Samarqand', callback_data='samarqand'),
        InlineKeyboardButton(text = 'Navoiy', callback_data='navoiy'),
        InlineKeyboardButton(text = 'Surxandaryo', callback_data='surxandaryo')
        
    ],
    [
        InlineKeyboardButton(text = 'Qashqadaryo', callback_data='qashqadaryo'),
        InlineKeyboardButton(text = 'Buxoro', callback_data='buxoro'),
        InlineKeyboardButton(text = 'Xorazm', callback_data='xorazm')
        
    ],
    [
        InlineKeyboardButton(text = 'Qoraqalpog\'iston', callback_data='qoraqalpogiston')
    ]

]

namoz_times = InlineKeyboardMarkup(inline_keyboard=namoz_buttons)
#toshkent---
toshkent_buttons = [
    [
        InlineKeyboardButton(text='Toshkent', callback_data='toshkent_uz')
    ],

    [
        InlineKeyboardButton(text='Angren', callback_data='angren'),
        InlineKeyboardButton(text='Piskent', callback_data='piskent'),
        InlineKeyboardButton(text='Bekobod', callback_data='bekobod')
    ],

    [
        InlineKeyboardButton(text='Parkent', callback_data='parkent'),
        InlineKeyboardButton(text='G\'azalkent', callback_data='gazalkent'),
        InlineKeyboardButton(text='Olmaliq', callback_data='olmaliq')
    ],
    
    [
        InlineKeyboardButton(text='Nurafshon', callback_data='nurafshon'),
        InlineKeyboardButton(text='Yangiyo\'ol', callback_data='yangiyol'),
        InlineKeyboardButton(text='Bo\'ko', callback_data='boka')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
toshkent_tuman = InlineKeyboardMarkup(inline_keyboard=toshkent_buttons)

#namangan------------------------------------------------------------------------
namangan_buttons  = [
    [
        InlineKeyboardButton(text='Namangan', callback_data='namangan_uz'),
        InlineKeyboardButton(text='Pop', callback_data='pop1'),
        InlineKeyboardButton(text='Chortoq', callback_data='chortoq')
    ],
    [
        InlineKeyboardButton(text='Chust', callback_data='chust'),
        InlineKeyboardButton(text='Uchqorg\'on', callback_data='uchqorgon'),
        InlineKeyboardButton(text='Mingbuloq', callback_data='mingbuloq')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
namangan_tuman = InlineKeyboardMarkup(inline_keyboard=namangan_buttons)

#andijon------------------------------------------------------------------------
andijon_buttons = [
    [
        InlineKeyboardButton(text='Andijon', callback_data='andijon_uz')
    ],
[
        InlineKeyboardButton(text='Xonobod', callback_data='xonobod'),
        InlineKeyboardButton(text='Xo\'jaobod', callback_data='xojaobod'),
        InlineKeyboardButton(text='Asaka', callback_data='asaka')
    ],
    [
        InlineKeyboardButton(text='Marhamat', callback_data='marhamat'),
        InlineKeyboardButton(text='Poytug\'', callback_data='paytug'),
        InlineKeyboardButton(text='Bo\'ston', callback_data='boston')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
andijon_tuman = InlineKeyboardMarkup(inline_keyboard=andijon_buttons)
#fargona------------------------------------------------------------------------
fargona_buttons = [
    [
        InlineKeyboardButton(text='Farg\'ona', callback_data='fargona_uz')
    ],
[
        InlineKeyboardButton(text='Qo\'qon', callback_data='qoqon'),
        InlineKeyboardButton(text='Marg\'ilon', callback_data='margilon'),
        InlineKeyboardButton(text='Quva', callback_data='quva')
    ],
    [
        InlineKeyboardButton(text='Rishton', callback_data='rishton'),
        InlineKeyboardButton(text='Bog\'dod', callback_data='bogdod'),
        InlineKeyboardButton(text='Oltiariq', callback_data='oltiariq')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
fargona_tuman = InlineKeyboardMarkup(inline_keyboard=fargona_buttons)
#Jizzax------------------------------------------------------------------------
jizzax_buttons = [
    [
        InlineKeyboardButton(text='Jizzax', callback_data='jizzax_uz')
    ],
    [
        InlineKeyboardButton(text='Forish', callback_data='forish'),
        InlineKeyboardButton(text='G\'allaorol', callback_data='gallaorol')
    ],
    [
        InlineKeyboardButton(text='Do\'stlik', callback_data='dostlik'),
        InlineKeyboardButton(text='Zomin', callback_data='zomin')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
jizzax_tuman = InlineKeyboardMarkup(inline_keyboard=jizzax_buttons)
#Surxandaryo------------------------------------------------------------------------
surxandaryo_buttons = [
    [
        InlineKeyboardButton(text='Termiz', callback_data='termiz')
    ],
    [
        InlineKeyboardButton(text='Sherobod', callback_data='sherobod'),
        InlineKeyboardButton(text='Boysun', callback_data='boysun')
    ],
    [
        InlineKeyboardButton(text='Denov', callback_data='denov'),
        InlineKeyboardButton(text='Sho\'rchi', callback_data='shorchi')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
surxandaryo_tuman = InlineKeyboardMarkup(inline_keyboard=surxandaryo_buttons)
#Buxoro------------------------------------------------------------------------
buxoro_buttons = [
    [
        InlineKeyboardButton(text='Buxoro', callback_data='buxoro_uz')
    ],
    [
        InlineKeyboardButton(text='G\'jduvon', callback_data='gijduvon'),
        InlineKeyboardButton(text='Jondor', callback_data='jondor')
    ],
    [
        InlineKeyboardButton(text='Qorako\'l', callback_data='qorakol'),
        InlineKeyboardButton(text='Gazli', callback_data='gazli')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
buxoro_tuman = InlineKeyboardMarkup(inline_keyboard=buxoro_buttons)

#Navoiy------------------------------------------------------------------------
navoiy_buttons = [
    [
        InlineKeyboardButton(text='Navoiy', callback_data='navoiy_uz')
    ],
    [
        InlineKeyboardButton(text='Zarafshon', callback_data='zarafshon'),
        InlineKeyboardButton(text='Konimex', callback_data='konimex')
    ],
    [
        InlineKeyboardButton(text='Uchquduq', callback_data='uchquduq'),
        InlineKeyboardButton(text='Nurota', callback_data='nurota')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
navoiy_tuman = InlineKeyboardMarkup(inline_keyboard=navoiy_buttons)

#Qashqadaryo------------------------------------------------------------------------
qashqadaryo_buttons = [
    [
        InlineKeyboardButton(text='Qarshi', callback_data='qarshi')
    ],
    [
        InlineKeyboardButton(text='Dehqonobod', callback_data='dehqonobod'),
        InlineKeyboardButton(text='Muborak', callback_data='muborak')
    ],
    [
        InlineKeyboardButton(text='Shahrisabz', callback_data='shahrisabz'),
        InlineKeyboardButton(text='G\'uzor', callback_data='guzor')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
qashqadaryo_tuman = InlineKeyboardMarkup(inline_keyboard=qashqadaryo_buttons)

#Sirdaryo------------------------------------------------------------------------
sirdaryo_buttons = [
    [
        InlineKeyboardButton(text='Sirdaryo', callback_data='sirdaryo_uz')
    ],
    [
        InlineKeyboardButton(text='Guliston', callback_data='guliston'),
        InlineKeyboardButton(text='Sardoba', callback_data='sardoba')
    ],
    [
        InlineKeyboardButton(text='Boyovut', callback_data='boyovut'),
        InlineKeyboardButton(text='Paxtaobod', callback_data='paxtaobod')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
sirdaryo_tuman = InlineKeyboardMarkup(inline_keyboard=sirdaryo_buttons)

#samarqand------------------------------------------------------------------------
samarqand_buttons = [
    [
        InlineKeyboardButton(text='Samarqand', callback_data='samarqand_uz')
    ],
        [
        InlineKeyboardButton(text='Ishtixon', callback_data='ishtixon'),
        InlineKeyboardButton(text='Mirbozor', callback_data='mirbozor')
    ],
    [
        InlineKeyboardButton(text='Kattaqorg\'on', callback_data='kattaqorgon'),
        InlineKeyboardButton(text='Urgut', callback_data='urgut')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
samarqand_tuman = InlineKeyboardMarkup(inline_keyboard=samarqand_buttons)

#Qoraqalpog'iston------------------------------------------------------------------------
qoraqalpogiston_buttons = [
    [
        InlineKeyboardButton(text='Nukus', callback_data='nukus')
    ],
    [
        InlineKeyboardButton(text='Mo\'ynoq', callback_data='moynoq'),
        InlineKeyboardButton(text='Taxtako\'pir', callback_data='taxtakopir')
    ],
    [
        InlineKeyboardButton(text='To\'rtko\'l', callback_data='tortkol'),
        InlineKeyboardButton(text='Qo\'ng\'irot', callback_data='qongirot')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
qoraqalpogiston_tuman = InlineKeyboardMarkup(inline_keyboard=qoraqalpogiston_buttons)

#Xorazm------------------------------------------------------------------------
xorazm_buttons = [
    [
        InlineKeyboardButton(text='Urganch', callback_data='urganch')
    ],
    [
        InlineKeyboardButton(text='Hazorasp', callback_data='hazorasp'),
        InlineKeyboardButton(text='Xonqa', callback_data='xonqa')
    ],
    [
        InlineKeyboardButton(text='Yangibozor', callback_data='yangibozor'),
        InlineKeyboardButton(text='Shovot', callback_data='shovot')
    ],
    [
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
]
xorazm_tuman = InlineKeyboardMarkup(inline_keyboard=xorazm_buttons)

#full_taqvim------------------------------------------------------------------
def get_tuman_markup(tuman_nomi):
    full_taqvim = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Oylik Taqvim', callback_data=f"full_taqvim:{tuman_nomi}"),
        InlineKeyboardButton(text='Orqaga', callback_data='back_to_main')
    ]
])
    return full_taqvim
#Ilm maskani btni uchun-----------------------------------------------------
ilm_markup = [
    [
        InlineKeyboardButton(text='Namoz', callback_data='namoz'),
        InlineKeyboardButton(text='Ro\'za', callback_data='roza')
    ],
    [
        InlineKeyboardButton(text='Haj', callback_data='haj'),
        InlineKeyboardButton(text='Zakot', callback_data='zakot')
    ]
]
ilm_maskani = InlineKeyboardMarkup(inline_keyboard=ilm_markup)
