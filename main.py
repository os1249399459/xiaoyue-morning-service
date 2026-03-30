#!/usr/bin/env python3
"""
小月早安服务 - 每天早上发送日语学习消息
温柔姐姐风格，带高低音标注，融入生活吐槽

运行模式：
- python main.py 生成消息并保存到 output.txt
- 由外部服务（如OpenClaw）读取并发送
"""

import os
import sys
import random
import requests
from datetime import datetime
from config import (
    TELEGRAM_USER_ID,
    WEATHER_CITY,
    XIAOYUE_PROFILE,
    BENTO_RECIPES,
    COLORS,
    SONGS,
    DAILY_WORDS,
)

# 输出文件路径
OUTPUT_FILE = os.path.expanduser("~/.openclaw/workspace/xiaoyue-morning-service/output.txt")

# 日期词汇
MONTH_WORDS = {
    1: {"cn": "一月", "jp": "一月", "romaji": "ichigatsu", "pitch": "i↘chi|gatsu"},
    2: {"cn": "二月", "jp": "二月", "romaji": "nigatsu", "pitch": "ni↘gatsu"},
    3: {"cn": "三月", "jp": "三月", "romaji": "sangatsu", "pitch": "san↗gatsu"},
    4: {"cn": "四月", "jp": "四月", "romaji": "shigatsu", "pitch": "shi↘gatsu"},
    5: {"cn": "五月", "jp": "五月", "romaji": "gogatsu", "pitch": "go↘gatsu"},
    6: {"cn": "六月", "jp": "六月", "romaji": "rokugatsu", "pitch": "ro↘ku|gatsu"},
    7: {"cn": "七月", "jp": "七月", "romaji": "shichigatsu", "pitch": "shi↘chi|gatsu"},
    8: {"cn": "八月", "jp": "八月", "romaji": "hachigatsu", "pitch": "ha↘chi|gatsu"},
    9: {"cn": "九月", "jp": "九月", "romaji": "kugatsu", "pitch": "ku↘gatsu"},
    10: {"cn": "十月", "jp": "十月", "romaji": "jugatsu", "pitch": "ju↘gatsu"},
    11: {"cn": "十一月", "jp": "十一月", "romaji": "juichigatsu", "pitch": "ju↘ichi|gatsu"},
    12: {"cn": "十二月", "jp": "十二月", "romaji": "junigatsu", "pitch": "ju↘ni|gatsu"},
}

DAY_WORDS = {
    0: {"cn": "星期日", "jp": "日曜日", "romaji": "nichiyōbi", "pitch": "ni↘chi|yō|bi"},
    1: {"cn": "星期一", "jp": "月曜日", "romaji": "getsuyōbi", "pitch": "getsu↗yō|bi"},
    2: {"cn": "星期二", "jp": "火曜日", "romaji": "kayōbi", "pitch": "ka↘yō|bi"},
    3: {"cn": "星期三", "jp": "水曜日", "romaji": "suiyōbi", "pitch": "su↘i|yō|bi"},
    4: {"cn": "星期四", "jp": "木曜日", "romaji": "mokuyōbi", "pitch": "mo↘ku|yō|bi"},
    5: {"cn": "星期五", "jp": "金曜日", "romaji": "kinyōbi", "pitch": "ki↘n|yō|bi"},
    6: {"cn": "星期六", "jp": "土曜日", "romaji": "doyōbi", "pitch": "do↘yō|bi"},
}

# 天气词汇
WEATHER_WORDS = {
    "Clear": {"cn": "晴天", "jp": "晴れ", "romaji": "hare", "pitch": "ha↘re"},
    "Sunny": {"cn": "晴天", "jp": "晴れ", "romaji": "hare", "pitch": "ha↘re"},
    "Cloudy": {"cn": "多云", "jp": "曇り", "romaji": "kumori", "pitch": "ku↘mo|ri"},
    "Overcast": {"cn": "阴天", "jp": "曇天", "romaji": "unten", "pitch": "u↘n|ten"},
    "Rain": {"cn": "雨天", "jp": "雨", "romaji": "ame", "pitch": "a↘me"},
    "Light rain": {"cn": "小雨", "jp": "小雨", "romaji": "kosame", "pitch": "ko↘sa|me"},
    "Heavy rain": {"cn": "大雨", "jp": "大雨", "romaji": "ōame", "pitch": "ō↘a|me"},
    "Snow": {"cn": "雪", "jp": "雪", "romaji": "yuki", "pitch": "yu↘ki"},
    "Fog": {"cn": "雾", "jp": "霧", "romaji": "kiri", "pitch": "ki↘ri"},
}


def get_weather(city: str) -> dict:
    """获取天气信息"""
    try:
        url = f"http://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            current = data.get("current_condition", [{}])[0]
            return {
                "temp": current.get("temp_C", "N/A"),
                "weather": current.get("weatherDesc", [{"value": "Unknown"}])[0].get("value", "Unknown"),
                "humidity": current.get("humidity", "N/A"),
                "feels_like": current.get("FeelsLikeC", "N/A"),
            }
    except Exception as e:
        print(f"天气查询失败: {e}")
    return {"temp": "N/A", "weather": "Unknown", "humidity": "N/A", "feels_like": "N/A"}


def get_news() -> str:
    """获取今日趣闻（简化版）"""
    # 这里可以接入新闻API，暂时用静态内容
    news_items = [
        "日本樱花季开始了，东京的樱花已经盛开~",
        "春天到了，好多地方的樱花都开了呢！",
        "最近天气变暖了，适合出门走走~",
        "春天是学习的好季节呢~",
    ]
    return random.choice(news_items)


def get_life_complaint() -> str:
    """随机生活吐槽"""
    complaints = [
        "姐姐最近找兼职，发现附近只有外卖骑手在招人...问题是姐姐不会骑电动车啊啊啊！",
        "房租和信用卡账单都要到期了...怎么办呢呜呜",
        "姐姐的伞放便利店门口被偷了...明明是普通的透明伞，为什么有人会偷啊！",
        "最近打 Slay the Spire 老是输...运气太差了",
        "出门忘带钥匙了，房东又不在...",
        "便利店打工又没被录用...姐姐只能继续找工作了",
        "天气变好了，但姐姐没钱出门呜呜",
    ]
    return random.choice(complaints)


def generate_message() -> str:
    """生成早安消息"""
    now = datetime.now()
    month = now.month
    day = now.day
    weekday = now.weekday()

    # 获取日期词汇
    month_word = MONTH_WORDS.get(month, {})
    day_word = {"cn": f"{day}日", "jp": f"{day}日", "romaji": f"{day}nichi", "pitch": f"{day}↘ni|chi"}
    weekday_word = DAY_WORDS.get(weekday, {})

    # 获取天气
    weather = get_weather(WEATHER_CITY)
    weather_word = WEATHER_WORDS.get(weather.get("weather", "Unknown"), 
                                      {"cn": weather.get("weather", "Unknown"), "jp": "天気", "romaji": "tenki", "pitch": "ten↗ki"})

    # 随机选择内容
    recipe = random.choice(BENTO_RECIPES)
    color = random.choice(COLORS)
    song = random.choice(SONGS)
    daily_word = random.choice(DAILY_WORDS)

    # 构建消息
    message = f"""🌙 弟弟~ おはよう|ございます (o↘hayō|goza↗imasu)

今天也是美好的一天呢，有没有睡个好觉呀？姐姐来陪你学日语咯~

📅 今天是{month_word.get('cn', f'{month}月')}{day}日，{weekday_word.get('cn', '星期X')}呢~
新的一周开始了，弟弟有什么计划吗？
{month_word.get('cn', '')} | {month_word.get('jp', '')} | {month_word.get('romaji', '')} ({month_word.get('pitch', '')})
{weekday_word.get('cn', '')} | {weekday_word.get('jp', '')} | {weekday_word.get('romaji', '')} ({weekday_word.get('pitch', '')})

🌤️ 上海今天{weather.get('temp', 'N/A')}度，{weather_word.get('cn', weather.get('weather', 'Unknown'))}~
{weather_word.get('cn', '')} | {weather_word.get('jp', '')} | {weather_word.get('romaji', '')} ({weather_word.get('pitch', '')})
早晚有点凉，记得多穿一件哦！姐姐会担心你的~

🍱 今天姐姐教你做——{recipe['name']}！
{recipe['name']} | {recipe['name_jp']} | {recipe['name_romaji']} ({recipe['pitch']})

食材词汇：
"""
    for ing in recipe['ingredients']:
        message += f"  {ing['cn']} | {ing['jp']} | {ing['romaji']} ({ing['pitch']})\n"

    message += f"""
做法简单，弟弟肯定能学会~

🎨 颜色词：{color['cn']}~
{color['cn']} | {color['jp']} | {color['romaji']} ({color['pitch']})

🎵 今日歌曲推荐——{song['cn']}（{song['source']}）
{song['cn']} | {song['jp']} | {song['romaji']} ({song['pitch']})

🌸 {get_news()}

💬 {get_life_complaint()}

顺便学一个词：
{daily_word['cn']} | {daily_word['jp']} | {daily_word['romaji']} ({daily_word['pitch']})

💪 今日鼓励：
きょうも|がんばってね (kyō↘mo|gan↘batte|ne)
「今天也要加油哦」——虽然姐姐有点倒霉，但还是要努力活下去！

明天见咯弟弟~ 🌙"""

    return message


def send_telegram_message(message: str, bot_token: str = None) -> bool:
    """发送Telegram消息"""
    bot_token = bot_token or os.environ.get("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        print("错误: 未找到Telegram Bot Token")
        return False

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": TELEGRAM_USER_ID,
        "text": message,
        "parse_mode": "HTML",
    }

    try:
        response = requests.post(url, data=data, timeout=30)
        if response.status_code == 200:
            print("消息发送成功！")
            return True
        else:
            print(f"发送失败: {response.text}")
            return False
    except Exception as e:
        print(f"发送异常: {e}")
        return False


def main():
    """主函数 - 生成消息并保存"""
    message = generate_message()
    
    # 保存到文件（供外部服务读取）
    output_dir = os.path.dirname(OUTPUT_FILE)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(message)
    
    print(f"✅ 消息已保存到: {OUTPUT_FILE}")
    print(message)


if __name__ == "__main__":
    main()