import datetime

def create_srt_template(filename="subtitle.srt"):
    """Creates a sample SRT file template."""
    content = [
        "1",
        "00:00:01,000 --> 00:00:04,000",
        "مرحباً بك في هذا الفيديو التعليمي.",
        "",
        "2",
        "00:00:04,500 --> 00:00:08,000",
        "سنقوم اليوم بتعلم كيفية استخدام Termux.",
        "",
        "3",
        "00:00:08,500 --> 00:00:12,000",
        "تأكد من تثبيت الحزم المطلوبة أولاً."
    ]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))
    return filename

file_path = create_srt_template()
print(f"File created: {file_path}")

