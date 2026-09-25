#!/bin/bash
# التأكد من وجود اسم ملف الفيديو
if [ -z "$1" ]; then
  echo "الرجاء تحديد اسم ملف الفيديو. مثال: ./auto_srt.sh video.mp4"
  exit 1
fi

# تشغيل whisper
whisper "$1" --model tiny --output_format srt
echo "تم إنشاء ملف الترجمة!"


