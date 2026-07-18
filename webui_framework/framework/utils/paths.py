from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
SCREENSHOT_DIR = ARTIFACTS_DIR / "screenshots"
VIDEO_DIR = ARTIFACTS_DIR / "videos"
CONSOLE_DIR = ARTIFACTS_DIR / "console"


def ensure_dirs() -> None:
    for d in (ARTIFACTS_DIR, SCREENSHOT_DIR, VIDEO_DIR, CONSOLE_DIR):
        d.mkdir(parents=True, exist_ok=True)
