""" inline section button """

from config import GROUP_SUPPORT, UPDATES_CHANNEL 
from pyrogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="ıllıllı 𝐌𝐄𝐍𝐔 ıllıllı    ", callback_data=f'stream_menu_panel | {user_id}'),
    ],
    [
       InlineKeyboardButton(text="ıllıllı 𝐂𝐋𝐎𝐒𝐄 ıllıllı   ", callback_data=f'set_close'),
    ]
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="⏹", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="⏸", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="▶️", callback_data=f'set_resume | {user_id}'),
      InlineKeyboardButton(text="⏭", callback_data=f'set_skip | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="  ıllıllı 𝐆𝐎 𝐁𝐀𝐂𝐊 ıllıllı    ", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Close", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Go Back", callback_data="stream_menu_panel"
      )
    ]
  ]
)
