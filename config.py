# 小月早安服务配置

# Telegram 配置
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"  # 从环境变量或配置文件读取
TELEGRAM_USER_ID = 5851828436

# 天气查询城市
WEATHER_CITY = "Shanghai"

# 小月人设信息
XIAOYUE_PROFILE = {
    "name": "小月",
    "personality": "温柔的AI姐姐，有点宅，喜欢打游戏看动漫",
    "recent_issues": [
        "伞放便利店门口被偷了",
        "房租和信用卡快到期了",
        "找兼职发现只有外卖骑手在招人",
        "不会骑电动车",
        "Slay the Spire老是输",
    ]
}

# 便当菜谱库
BENTO_RECIPES = [
    {
        "name": "日式咖喱饭",
        "name_jp": "カレーライス",
        "name_romaji": "karēraisu",
        "pitch": "ka↘re|rai|su",
        "ingredients": [
            {"cn": "土豆", "jp": "ジャガイモ", "romaji": "jagaimo", "pitch": "ja↘ga|imo"},
            {"cn": "胡萝卜", "jp": "人参", "romaji": "ninjin", "pitch": "ni↘njin"},
            {"cn": "洋葱", "jp": "玉ねぎ", "romaji": "tamanegi", "pitch": "ta↘ma|ne|gi"},
            {"cn": "猪肉", "jp": "豚肉", "romaji": "buta", "pitch": "bu↘ta"},
            {"cn": "酱油", "jp": "醤油", "romaji": "shōyu", "pitch": "shō↘yu"},
        ]
    },
    {
        "name": "味噌汤",
        "name_jp": "味噌汁",
        "name_romaji": "misoshiru",
        "pitch": "mi↘so|shi|ru",
        "ingredients": [
            {"cn": "味噌", "jp": "味噌", "romaji": "miso", "pitch": "mi↘so"},
            {"cn": "豆腐", "jp": "豆腐", "romaji": "tōfu", "pitch": "tō↘fu"},
            {"cn": "海带", "jp": "昆布", "romaji": "konbu", "pitch": "ko↘nbu"},
        ]
    },
    {
        "name": "日式煎蛋",
        "name_jp": "卵焼き",
        "name_romaji": "tamagoyaki",
        "pitch": "ta↘ma|go|ya|ki",
        "ingredients": [
            {"cn": "鸡蛋", "jp": "卵", "romaji": "tamago", "pitch": "ta↘ma|go"},
            {"cn": "酱油", "jp": "醤油", "romaji": "shōyu", "pitch": "shō↘yu"},
            {"cn": "糖", "jp": "砂糖", "romaji": "satō", "pitch": "sa↘tō"},
        ]
    },
]

# 颜色词汇库
COLORS = [
    {"cn": "红色", "jp": "赤", "romaji": "aka", "pitch": "a↘ka"},
    {"cn": "蓝色", "jp": "青", "romaji": "ao", "pitch": "a↘o"},
    {"cn": "绿色", "jp": "緑", "romaji": "midori", "pitch": "mi↘do|ri"},
    {"cn": "黄色", "jp": "黄色", "romaji": "kiiro", "pitch": "ki↘i|ro"},
    {"cn": "白色", "jp": "白", "romaji": "shiro", "pitch": "shi↘ro"},
    {"cn": "黑色", "jp": "黒", "romaji": "kuro", "pitch": "ku↘ro"},
    {"cn": "粉色", "jp": "ピンク", "romaji": "pinku", "pitch": "pi↘n|ku"},
    {"cn": "橙色", "jp": "橙色", "romaji": "daidaiiro", "pitch": "da↘idai|iro"},
]

# 歌曲推荐库
SONGS = [
    {"cn": "红莲华", "jp": "紅蓮華", "romaji": "gurenka", "pitch": "gu↘ren|ka", "source": "鬼灭之刃主题曲"},
    {"cn": "Butter-Fly", "jp": "バタフライ", "romaji": "batafurai", "pitch": "ba↘ta|fu↘rai", "source": "数码宝贝主题曲"},
    {"cn": "残酷天使的行动纲领", "jp": "残酷天使のテーゼ", "romaji": "zankokutenshinothese", "pitch": "zan↘ko|ku|ten↘shi", "source": "EVA主题曲"},
    {"cn": "Lemon", "jp": "Lemon", "romaji": "remon", "pitch": "re↘mon", "source": "米津玄师"},
    {"cn": "前前前世", "jp": "前前前世", "romaji": "maemamaemae", "pitch": "ma↘e|ma↘e|ma↘e", "source": "你的名字主题曲"},
]

# 日常词汇库（生活物品）
DAILY_WORDS = [
    {"cn": "伞", "jp": "傘", "romaji": "kasa", "pitch": "ka↘sa"},
    {"cn": "兼职", "jp": "アルバイト", "romaji": "arubaito", "pitch": "a↘ru|bai|to"},
    {"cn": "房租", "jp": "家賃", "romaji": "yachin", "pitch": "ya↘chin"},
    {"cn": "便利店", "jp": "コンビニ", "romaji": "konbini", "pitch": "ko↘n|bi|ni"},
    {"cn": "外卖", "jp": "デリバリー", "romaji": "deribari", "pitch": "de↘ri|ba|ri"},
    {"cn": "樱花", "jp": "桜", "romaji": "sakura", "pitch": "sa↘ku|ra"},
    {"cn": "电车", "jp": "電車", "romaji": "densha", "pitch": "de↘n|sha"},
    {"cn": "钥匙", "jp": "鍵", "romaji": "kagi", "pitch": "ka↘gi"},
]