Markdown# Electronic Voting System / سیستم رای‌گیری الکترونیکی

[English](#english) | [فارسی](#فارسی)

---

## English

A simple, clean, and user-friendly **desktop Electronic Voting System** built with **Python** and **PyQt5**.

Perfect for small elections, classroom votes, clubs, or local events.

### Features

- Welcome screen with modern dark theme
- Configurable number of candidates (1–1000)
- Choose how many top winners to highlight
- Limit votes per voter (lock after N votes)
- Add / remove candidate names easily
- Voter registration by name
- One vote per candidate per voter (no double voting)
- Automatic lock after reaching the vote limit
- Show / hide live vote counts
- View list of all registered voters
- Final ranked results with highlighted winners
- Fully offline (no internet required)
- Dark modern UI

### Screenshots

| Welcome Screen | Election Setup |
|:---:|:---:|
| ![Welcome](screenshots/01_electronic_voting_system.png) | ![Setup](screenshots/02_Ssetup.png) |

| Candidates | Delete Candidate |
|:---:|:---:|
| ![Candidates](screenshots/03_cndidates.png) | ![Delete](screenshots/04_delete_last_candidate.png) |

| Voting Menu | Show Voters |
|:---:|:---:|
| ![Voting](screenshots/05_voting_menu.png) | ![Voters](screenshots/06_show_voters.png) |

| Show Votes | Final Results |
|:---:|:---:|
| ![Votes](screenshots/07_show_candidates_votes.png) | ![Winner](screenshots/08_show_winner.png) |

### Requirements

- Python 3.8 or higher
- PyQt5

### Installation

```bash
# Clone the repository
git clone https://github.com/mani-maz/electronic-voting-system.git
cd electronic-voting-system

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
How to Run
Bashpython voting_system.py
Download Ready-to-Use Version (Windows)
You can download the pre-built .exe file from the Releases section.
How to Use

Welcome Screen → Click Continue
Nomination Screen
Set number of candidates
Set number of winners to highlight
Set maximum votes allowed per voter
Enter candidate names (press Enter after each name)
You can delete the last candidate or view the list
Click Start Voting

Voting Screen
Enter voter name and press Enter
Click on candidates to vote (each candidate can be selected only once)
After reaching the vote limit, voting locks automatically
Use Show Votes / Hide Votes to toggle live counts
Use Show Voters to see the list of voters
Click END when voting is finished to see the final ranked results


Project Structure
textelectronic-voting-system/
├── voting_system.py      # Main application
├── requirements.txt      # Dependencies
├── LICENSE               # MIT License
├── .gitignore
├── screenshots/          # Application screenshots
└── README.md             # This file
License
This project is licensed under the MIT License — see the LICENSE [blocked] file for details.
Author
mani_maz

Created with ❤️

فارسی
یک سیستم رای‌گیری الکترونیکی دسکتاپ ساده، تمیز و کاربرپسند که با پایتون و PyQt5 نوشته شده است.
مناسب برای انتخابات کوچک، رأی‌گیری کلاسی، باشگاه‌ها یا رویدادهای محلی.
ویژگی‌ها

صفحه خوش‌آمدگویی با تم تاریک مدرن
قابل تنظیم تعداد نامزدها (از ۱ تا ۱۰۰۰)
انتخاب تعداد برندگان برتر برای هایلایت
محدودیت تعداد رأی برای هر رأی‌دهنده
اضافه و حذف آسان نام نامزدها
ثبت‌نام رأی‌دهنده با نام
جلوگیری از رأی تکراری به یک نامزد
قفل خودکار بعد از رسیدن به حد رأی
نمایش / مخفی کردن تعداد رأی‌ها به صورت زنده
مشاهده لیست تمام رأی‌دهندگان
نمایش نتایج نهایی رتبه‌بندی‌شده با هایلایت برندگان
کاملاً آفلاین (بدون نیاز به اینترنت)
رابط کاربری تاریک و مدرن

تصاویر برنامه













صفحه خوش‌آمدگوییتنظیمات انتخابات













نامزدهاحذف نامزد













صفحه رأی‌گیرینمایش رأی‌دهندگان













نمایش رأی‌هانتایج نهایی
نیازمندی‌ها

پایتون ۳.۸ یا بالاتر
کتابخانه PyQt5

نصب
Bash# کلون کردن مخزن
git clone https://github.com/mani-maz/electronic-voting-system.git
cd electronic-voting-system

# (اختیاری) ساخت محیط مجازی
python -m venv venv
source venv/bin/activate        # لینوکس / مک
# venv\Scripts\activate         # ویندوز

# نصب وابستگی‌ها
pip install -r requirements.txt
نحوه اجرا
Bashpython voting_system.py
دانلود نسخه آماده (ویندوز)
می‌توانید فایل اجرایی .exe را از بخش Releases دانلود کنید.
نحوه استفاده

صفحه خوش‌آمدگویی → روی Continue کلیک کنید
صفحه نامزدی
تعداد نامزدها را مشخص کنید
تعداد برندگان برای هایلایت را تنظیم کنید
حداکثر رأی مجاز برای هر رأی‌دهنده را تعیین کنید
نام نامزدها را وارد کنید (بعد از هر نام Enter بزنید)
می‌توانید آخرین نامزد را حذف کنید یا لیست را ببینید
روی Start Voting کلیک کنید

صفحه رأی‌گیری
نام رأی‌دهنده را وارد کنید و Enter بزنید
روی نامزدها کلیک کنید (هر نامزد فقط یک‌بار قابل انتخاب است)
بعد از رسیدن به حد رأی، رأی‌گیری به‌طور خودکار قفل می‌شود
از دکمه‌های Show Votes / Hide Votes برای نمایش یا مخفی کردن تعداد رأی‌ها استفاده کنید
با Show Voters لیست رأی‌دهندگان را ببینید
وقتی رأی‌گیری تمام شد روی END کلیک کنید تا نتایج نهایی نمایش داده شود


ساختار پروژه
textelectronic-voting-system/
├── voting_system.py      # برنامه اصلی
├── requirements.txt      # وابستگی‌ها
├── LICENSE               # لایسنس MIT
├── .gitignore
├── screenshots/          # تصاویر برنامه
└── README.md             # این فایل
لایسنس
این پروژه تحت لایسنس MIT منتشر شده است — برای جزئیات فایل LICENSE [blocked] را ببینید.
نویسنده
mani_maz

ساخته شده با ❤️
