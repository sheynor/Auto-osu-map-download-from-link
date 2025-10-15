import os
import re
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# 📂 Куда сохранять карты (в Загрузки)
SAVE_DIR = os.path.expanduser("~/Загрузки/osu_beatmaps")
THREADS = 8  # количество потоков (можно увеличить для скорости)

os.makedirs(SAVE_DIR, exist_ok=True)

def extract_id(url: str):
    match = re.search(r"beatmapsets/(\d+)", url)
    return match.group(1) if match else None

def download_map(beatmap_id):
    url = f"https://catboy.best/d/{beatmap_id}"
    filename = os.path.join(SAVE_DIR, f"{beatmap_id}.osz")
    try:
        r = requests.get(url, stream=True, timeout=30)
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"✅ Скачано: {filename}")
    except Exception as e:
        print(f"❌ Ошибка при скачивании {beatmap_id}: {e}")

def main():
    with open("links.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    ids = [extract_id(url) for url in urls if extract_id(url)]
    print(f"Найдено {len(ids)} карт для скачивания\n")

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = [executor.submit(download_map, beatmap_id) for beatmap_id in ids]
        for _ in as_completed(futures):
            pass

    print("\n🎵 Все загрузки завершены!")
    print(f"Файлы сохранены в: {SAVE_DIR}")

if __name__ == "__main__":
    main()
