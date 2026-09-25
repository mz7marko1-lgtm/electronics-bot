# generator.py
def save_srt(filename, entries):
    with open(filename, 'w', encoding='utf-8') as f:
        for i, entry in enumerate(entries, 1):
            f.write(f"{i}\n")
            f.write(f"{entry['start']} --> {entry['end']}\n")
            f.write(f"{entry['text']}\n\n")
    print(f"تم حفظ الملف بنجاح باسم: {filename}")

# أضف الجمل والتوقيتات هنا (توقيت البداية --> توقيت النهاية)
subtitles = [
    {"start": "00:00:01,000", "end": "00:00:04,000", "text": "الجملة الأولى هنا"},
    {"start": "00:00:05,000", "end": "00:00:08,000", "text": "الجملة الثانية هنا"},
    {"start": "00:00:09,000", "end": "00:00:12,000", "text": "الجملة الثالثة هنا"}
]

save_srt("my_video.srt", subtitles)

