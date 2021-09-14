from os import path

from youtube_dl import YoutubeDL

from MusicMan.config import DURATION_LIMIT
from MusicMan.helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio[ext=m4a]",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}

ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"❌ **Video dengan durasi lebih dari** `{DURATION_LIMIT}` **menit tidak bisa diputar!**"
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"❌ **Video dengan durasi lebih dari** `{DURATION_LIMIT}` **menit tidak bisa diputar!**"
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
