import json
from pathlib import Path

PACKAGES_DIR = Path("media/packages")


def build_timeline(package: dict) -> list[dict]:
    timeline = []
    current_time = 0.0

    storyboard = package["video"].get("storyboard", [])

    for scene in storyboard:
        duration = float(scene.get("duration", 6))
        broll_file = scene.get("broll_file")

        if not broll_file:
            continue

        timeline.append({
            "scene": scene.get("scene"),
            "clip": broll_file,
            "start": current_time,
            "end": current_time + duration,
            "duration": duration,
            "subtitle": scene.get("subtitle", ""),
            "transition": "fade",
            "zoom": "slow",
        })

        current_time += duration

    return timeline


def main():
    packages = sorted(PACKAGES_DIR.glob("*.json"))

    if not packages:
        print("No packages found.")
        return

    for package_file in packages:
        with open(package_file, "r", encoding="utf-8") as f:
            package = json.load(f)

        timeline = build_timeline(package)

        package["video"]["timeline"] = timeline
        package["video"]["timeline_duration"] = sum(item["duration"] for item in timeline)

        with open(package_file, "w", encoding="utf-8") as f:
            json.dump(package, f, ensure_ascii=False, indent=2)

        print(f"{package['id']}: {len(timeline)} timeline clips")

    print("Timeline build completed.")


if __name__ == "__main__":
    main()