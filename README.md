# Auto-osu-map-download-from-link (made by ChatGPT)
# 🎶 osu! Beatmap Downloader (Python)

Скрипт для **автоматической загрузки карт osu! (.osz)** по списку ссылок из `links.txt`.  
Поддерживает многопоточность, не требует входа в аккаунт osu! и работает на **Linux / macOS / Windows**.

---

## 🚀 Возможности
- Скачивает все карты из списка ссылок `https://osu.ppy.sh/beatmapsets/...`
- Работает без браузера и логина (использует открытое зеркало [catboy.best](https://catboy.best))
- Сохраняет карты в папку `~/Загрузки/osu_beatmaps`
- Поддержка многопоточности (быстро качает десятки карт одновременно)
- Простой запуск в один клик

---

## 🧩 Требования
- **Python 3.8+**
- Модуль `requests`

Установка:
```bash
sudo pacman -S python-requests
# или
pip install requests
