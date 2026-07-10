# ==============================================
# BOT TREE FARM - HOÀN CHỈNH
# ==============================================

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import requests
import threading
from flask import Flask

TOKEN = "8616760362:AAHm1r-nBmbunneoOJm7WwzeHvQzfVJgBAI"
bot = telebot.TeleBot(TOKEN)

# 🔗 LINK ẢNH - THAY BẰNG LINK ẢNH TRỰC TIẾP KẾT THÚC .PNG/.JPG
LINK_ANH = "https://i.ibb.co/7x7DFnZ9/1783599852392" 

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
# GIỮ BOT LUÔN CHẠY (CHO RENDER/HOST MIỄN PHÍ)
# ==============================================
app = Flask(__name__)
@app.route('/')
def keep_alive(): return "✅ Bot Tree Farm đang hoạt động!"
def run(): app.run(host='0.0.0.0', port=8080)
threading.Thread(target=run, daemon=True).start()


# ==============================================
# KHỞI ĐỘNG BOT
# ==============================================
print("="*50)
print("✅ BOT TREE FARM ĐÃ CHẠY!")
print("🖼️  Ảnh trang trại đã gắn")
print("🔗 Mini App: https://treefarmapp.netlify.app/")
print("📋 Log chỉ ghi 1 lần cho mỗi người dùng")
print("="*50 + "\n")

bot.polling(none_stop=True)
