import os

base_url = os.getenv("BASE_URL", "unknown")
bot_username = os.getenv("BOT_USERNAME", "unknown")
bot_password = os.getenv("BOT_PASSWORD", "unknown")

reports = [
    {
        "name": "今日新单报表",
        "page": 208,
    },
    {
        "name": "延期出货明细表",
        "page": 220,
    },
    {
        "name": "宏智出货报表",
        "page": 210,
        "has_tail": False,
    },
    {
        "name": "技果出货报表",
        "page": 207,
        "has_tail": False,
    },
    {
        "name": "迅成出货报表",
        "page": 206,
        "has_tail": False,
    },
    {
        "name": "金安出货报表",
        "page": 212,
        "has_tail": False,
    },
    {
        "name": "长嘉出货报表",
        "page": 205,
        "has_tail": True,
    },
]
