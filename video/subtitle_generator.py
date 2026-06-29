import json
from pathlib import Path


PACKAGES_DIR = Path("media/packages")
OUTPUT_DIR = Path("media/subtitles")


def format_time(seconds: float) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def create_srt(subtitles: list[str], output_file: Path):
    output_file.parent.mkdir(parents=True, exist_ok=True)

    if not subtitles:
        subtitles = [""]

    total_duration = 60.0
    duration_per_line = total_duration / len(subtitles)

    with open(output_file, "w", encoding="utf-8") as f:
        current = 0.0

        for i, line in enumerate(subtitles, start=1):
            start = current
            end = current + duration_per_line

            f.write(f"{i}\n")
            f.write(f"{format_time(start)} --> {format_time(end)}\n")
            f.write(line.strip() + "\n\n")

            current = end


def main():
    packages = sorted(PACKAGES_DIR.glob("*.json"))

    if not packages:
        print("No packages found.")
        return

    for package_file in packages:

        with open(package_file, "r", encoding="utf-8") as f:
            package = json.load(f)

        package_id = package["id"]

        subtitles = package["video"].get("subtitle_lines", [])

        output_file = OUTPUT_DIR / f"{package_id}.srt"

        create_srt(subtitles, output_file)

        package["production"]["subtitle_file"] = str(output_file)

        with open(package_file, "w", encoding="utf-8") as f:
            json.dump(package, f, ensure_ascii=False, indent=2)

        print(f"Created: {output_file}")

    print("Subtitle generation completed.")


if __name__ == "__main__":
    main()