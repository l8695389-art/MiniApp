# ==============================================
# BOT TREE FARM - ĐÃ GẮN ẢNH MỚI
# ==============================================

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import requests

TOKEN = "8616760362:AAHm1r-nBmbunneoOJm7WwzeHvQzfVJgBAI"
bot = telebot.TeleBot(TOKEN)

# 🔗 LINK ẢNH TRANG TRẠI MỚI
LINK_ANH = "https://ibb.co/7x7DFnZ9"

# 📂 LƯU ID ĐÃ GHI LOG - KHÔNG LẶP LẠI
da_ghi_log = set()


# ==============================================
# HÀM GHI LOG CHỈ 1 LẦN
# ==============================================
def ghiLogTermux(user):
    user_id = user.id
    if user_id in da_ghi_log:
        return

    try:
        ip = requests.get("https://api.ipify.org?format=json", timeout=5).json()["ip"]
    except:
        ip = "Không lấy được IP"

    thoiGian = datetime.now().strftime("%d/%m/%Y | %H:%M:%S")
    ho_ten = f"{user.first_name} {user.last_name or ''}".strip()
    tai_khoan = f" (@{user.username})" if user.username else ""

    print("\n" + "="*50)
    print(f"📌 NGƯỜI DÙNG MỚI VÀO /start")
    print(f"⏰ Thời gian : {thoiGian}")
    print(f"👤 Tên       : {ho_ten}{tai_khoan}")
    print(f"🆔 ID        : {user_id}")
    print(f"🌐 Địa chỉ IP : {ip}")
    print("="*50 + "\n")

    da_ghi_log.add(user_id)


# ==============================================
# XỬ LÝ /start - GỬI ẢNH + NỘI DUNG + NÚT
# ==============================================
@bot.message_handler(commands=['start'])
def xuLyStart(message):
    ghiLogTermux(message.from_user)

    nut = InlineKeyboardMarkup(row_width=1)
    nut.add(InlineKeyboardButton(
        "🌳 MỞ TREE FARM",
        web_app=telebot.types.WebAppInfo(url="https://treefarmapp.netlify.app/")
    ))

    bot.send_photo(
        chat_id = message.chat.id,
        photo = LINK_ANH,
        caption = """Welcome to Tree Farm 🌾

Trồng trọt, làm nhiệm vụ mỗi ngày và tích xu đổi thưởng.

Mời bạn bè, leo bảng xếp hạng và rút kim cương khi đủ điều kiện.""",
        reply_markup = nut
    )


# ==============================================
# KHỞI ĐỘNG BOT
# ==============================================
print("="*50)
print("✅ BOT TREE FARM ĐÃ CHẠY!")
print("🖼️  Đã dùng ảnh trang trại hoạt hình mới")
print("🔗 Mini App: https://treefarmapp.netlify.app/")
print("📋 Log chỉ ghi 1 lần cho mỗi người dùng")
print("="*50 + "\n")

bot.polling(none_stop=True)
import threading
from flask import Flask
app = Flask(__name__)
@app.route('/')
def keep_alive(): return "Bot đang chạy!"
def run(): app.run(host='0.0.0.0', port=8080)
threading.Thread(target=run).start()
