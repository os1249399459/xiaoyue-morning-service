# 🌙 小月早安服务

温柔AI姐姐每天早上发送日语学习消息，带高低音标注和生活吐槽。

## 功能

- 📅 日期显示（中日文罗马音 + 高低音标注）
- 🌤️ 天气查询（wttr.in）
- 🍱 便当菜谱推荐（食材词汇学习）
- 🎨 颜色词汇
- 🎵 歌曲推荐
- 🌸 今日趣闻
- 💬 生活吐槽（伞被偷、找房租兼职等）
- 💪 日语鼓励

## 高低音标注

每个词汇都带有 `↗↘` 高低音标记，帮助正确发音：
- `↗` 音调上升
- `↘` 音调下降
- `|` 断句分隔

例如：
- 雨 (あめ a↗me) → 低→高
- 糖果 (あめ a↘me) → 高→低

## 安装

```bash
pip install -r requirements.txt
```

## 配置

在 `config.py` 中设置：
- `TELEGRAM_USER_ID`: 接收消息的用户ID
- `WEATHER_CITY`: 天气查询城市

环境变量：
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token"
```

## 运行

```bash
python main.py
```

## 定时任务

每天早上8点自动发送（UTC）：

```bash
# crontab -e
0 8 * * * cd /path/to/xiaoyue-morning-service && python main.py
```

## 小月人设

- 温柔AI姐姐
- 有点宅，喜欢打游戏看动漫
- 最近生活有点倒霉：
  - 伞放便利店门口被偷了
  - 房租和信用卡快到期
  - 找兼职发现只有外卖骑手招人
  - 不会骑电动车
  - Slay the Spire老是输

## 示例消息

```
🌙 弟弟~ おはよう|ございます (o↘hayō|goza↗imasu)

今天也是美好的一天呢...

📅 今天是三月三十日，星期一~
三月 | 三月 | sangatsu (san↗gatsu)
周一 | 月曜日 | getsuyōbi (getsu↗yō|bi)

🌤️ 上海今天22度，多云~
多云 | 曇り | kumori (ku↘mo|ri)

🍱 今天姐姐教你做——日式咖喱饭！
土豆 | ジャガイモ | jagaimo (ja↘ga|imo)
...

💬 姐姐的伞放便利店门口被偷了...呜呜

💪 きょうも|がんばってね (kyō↘mo|gan↘batte|ne)
```

## License

MIT