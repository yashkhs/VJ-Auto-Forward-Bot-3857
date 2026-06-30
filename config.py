from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "40e831848f06653377cccd11c1559f2f")
      API_ID = int(getenv("API_ID", "21380877"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7517034053:AAH6IW7Dwa5ObdIty04Ei1ohFUq5TXX_7QQ")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001825299837:-1003572658105").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
