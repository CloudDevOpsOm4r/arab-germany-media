import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class PexelsProvider:
    def __init__(self):
        self.api_key = os.getenv("PEXELS_API_KEY")
        self.base_url = "https://api.pexels.com/videos/search"

        if not self.api_key:
            raise ValueError("PEXELS_API_KEY is missing in .env")

    def search_videos(self, query: str, per_page: int = 3) -> list:
        headers = {
            "Authorization": self.api_key
        }

        params = {
            "query": query,
            "per_page": per_page,
            "orientation": "portrait"
        }

        response = requests.get(
            self.base_url,
            headers=headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        return data.get("videos", [])

    def download_video(self, url: str, output_file: Path) -> Path:
        output_file.parent.mkdir(parents=True, exist_ok=True)

        response = requests.get(url, timeout=60)
        response.raise_for_status()

        with open(output_file, "wb") as f:
            f.write(response.content)

        return output_file

    def get_best_video_url(self, video: dict) -> str:
        files = video.get("video_files", [])

        portrait_files = [
            f for f in files
            if f.get("width", 0) < f.get("height", 0)
        ]

        candidates = portrait_files or files

        if not candidates:
            return ""

        candidates = sorted(
            candidates,
            key=lambda f: f.get("width", 0) * f.get("height", 0),
            reverse=True
        )

        return candidates[0].get("link", "")