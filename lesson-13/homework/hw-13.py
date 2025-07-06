import datetime
import time
import re
import pytz

# 1. Age Calculator
def age_calculator():
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = datetime.datetime.strptime(birth_str, "%Y-%m-%d").date()
    today = datetime.date.today()
    delta = today - birth_date
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    print(f"Your age is: {years} years, {months} months, {days} days")

# 2. Days Until Next Birthday
def days_until_birthday():
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = datetime.datetime.strptime(birth_str, "%Y-%m-%d").date()
    today = datetime.date.today()
    next_birthday = birth_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_left = (next_birthday - today).days
    print(f"Days until next birthday: {days_left}")

# 3. Meeting Scheduler
def meeting_scheduler():
    now_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    duration_hours = int(input("Enter meeting duration (hours): "))
    duration_minutes = int(input("Enter meeting duration (minutes): "))
    start = datetime.datetime.strptime(now_str, "%Y-%m-%d %H:%M")
    end = start + datetime.timedelta(hours=duration_hours, minutes=duration_minutes)
    print("Meeting will end at:", end.strftime("%Y-%m-%d %H:%M"))

# 4. Timezone Converter
def timezone_converter():
    time_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_zone = input("Enter your current timezone (e.g., Asia/Tashkent): ")
    to_zone = input("Enter target timezone (e.g., US/Eastern): ")
    local_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    local_zone = pytz.timezone(from_zone)
    target_zone = pytz.timezone(to_zone)
    local_dt = local_zone.localize(local_time)
    target_dt = local_dt.astimezone(target_zone)
    print("Converted time:", target_dt.strftime("%Y-%m-%d %H:%M"))

# 5. Countdown Timer
def countdown_timer():
    future_str = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ")
    future_time = datetime.datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")
    print("Countdown started...")
    while True:
        now = datetime.datetime.now()
        if future_time <= now:
            print("Time's up!")
            break
        delta = future_time - now
        print("Time left:", str(delta).split(".")[0], end="\r")
        time.sleep(1)

# 6. Email Validator
def email_validator():
    email = input("Enter your email address: ")
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$"
    if re.match(pattern, email):
        print("Valid email!")
    else:
        print("Invalid email!")

# 7. Phone Number Formatter
def phone_formatter():
    phone = input("Enter 10-digit phone number: ")
    clean = re.sub(r"\D", "", phone)
    if len(clean) == 10:
        formatted = f"({clean[:3]}) {clean[3:6]}-{clean[6:]}"
        print("Formatted:", formatted)
    else:
        print("Invalid phone number.")

# 8. Password Strength Checker
def password_strength():
    pwd = input("Enter password: ")
    if (len(pwd) >= 8 and 
        re.search(r"[A-Z]", pwd) and 
        re.search(r"[a-z]", pwd) and 
        re.search(r"\d", pwd)):
        print("Strong password.")
    else:
        print("Weak password. Must contain at least 8 chars, 1 uppercase, 1 lowercase, and 1 digit.")

# 9. Word Finder
def word_finder():
    sample_text = """This is a sample text. You can search for a word in this text and see all occurrences of that word."""
    word = input("Enter word to find: ").lower()
    words = re.findall(r"\b" + re.escape(word) + r"\b", sample_text.lower())
    print(f"Occurrences of '{word}': {len(words)}")

# 10. Date Extractor
def date_extractor():
    text = input("Enter text with dates (format: YYYY-MM-DD): ")
    dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
    print("Found dates:", dates)

