import random
import string
from ast import ExceptHandler

from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InputMediaPhoto,
                            Message)
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS, lyrical
from strings import get_command
from Auput import (Apple, Resso, SoundCloud, Spotify, Telegram,
                        YouTube, app)
from Auput.core.call import Auput
from Auput.utils import seconds_to_min, time_to_seconds
from Auput.utils.channelplay import get_channeplayCB
from Auput.utils.database import is_video_allowed
from Auput.utils.decorators.language import languageCB
from Auput.utils.decorators.play import PlayWrapper
from Auput.utils.formatters import formats
from Auput.utils.inline.play import (livestream_markup,
                                          playlist_markup,
                                          slider_markup, track_markup)
from Auput.utils.inline.playlist import botplaylist_markup
from Auput.utils.logger import play_logs
from Auput.utils.stream.stream import stream


