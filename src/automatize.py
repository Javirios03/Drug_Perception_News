import datetime
from yt_dlp import YoutubeDL

today = datetime.date.today()

# Obtain the day in the format dd-mm-yy
day = today.strftime("%d/%m/%y")
# yesterday = (today - datetime.timedelta(days=1)).strftime("%d/%m/%y")

# Using yt-dlp, extract today's programme URL
with YoutubeDL({"extract_flat": True, "dump_single_json": True}) as ydl:
    info = ydl.extract_info("https://www.rtve.es/play/videos/telediario-2/", download=False)
    
entries = info.get("entries", [])

# Filter entries for today's date
url = None
for entry in entries:
    # if "title" in entry and day in entry["title"]:
    if "title" in entry and day in entry["title"]:
        url = entry.get("url")
        break

# If no URL found, raise an error
if not url:
    # raise ValueError(f"No URL found for the date {day}.")
    raise ValueError(f"No URL found for the date {day}.")

# Store the URL in a text file
with open("video_urls.txt", "a") as file:
    file.write(f"{day} - {url}\n")
