import subprocess
import sys

steps = [
    ("Collect news", "sources/rss_collector.py"),
    ("Score news", "ai/news_scorer.py"),
    ("Classify news", "ai/news_classifier.py"),
]

for name, script in steps:
    print(f"\n=== {name} ===")
    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"Failed: {script}")
        sys.exit(result.returncode)

print("\nPipeline completed successfully.")