import json
from pathlib import Path

from media.broll.provider import Broll

PACKAGES_DIR = Path("media/packages")
OUTPUT_DIR = Path("media/broll/videos")


def main():
    packages = sorted(PACKAGES_DIR.glob("*.json"))

    for package_file in packages:
        with open(package_file, "r", encoding="utf-8") as f:
            package = json.load(f)

        package_id = package["id"]
        storyboard = package["video"].get("storyboard", [])

        for scene in storyboard:
            scene_no = scene["scene"]
            query = scene["pexels_query"]

            output_file = OUTPUT_DIR / package_id / f"scene_{scene_no:02d}.mp4"

            if output_file.exists():
                print(f"Exists: {output_file}")
                continue

            print(f"Searching: {query}")
            videos = Broll.search_videos(query, 1)

            if not videos:
                print(f"No video found for: {query}")
                continue

            url = Broll.get_best_video_url(videos[0])
            Broll.download_video(url, output_file)

            scene["broll_file"] = str(output_file)
            print(f"Downloaded: {output_file}")

        with open(package_file, "w", encoding="utf-8") as f:
            json.dump(package, f, ensure_ascii=False, indent=2)

    print("B-roll download completed.")


if __name__ == "__main__":
    main()