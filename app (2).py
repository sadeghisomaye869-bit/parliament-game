import streamlit as st
import random

st.set_page_config(page_title="Parliament Game", layout="centered")

st.title("🎮 بازی قانون‌گذاری پارلمان")

if "stage" not in st.session_state:
    st.session_state.stage = 1
    st.session_state.score = 0

# -------------------------------
# مرحله ۱ – انتخاب طرح
# -------------------------------
if st.session_state.stage == 1:
    st.header("مرحله ۱: انتخاب طرح")

    bills = {
        "افزایش عوارض محصولات پرآب صادراتی": (3, 3, 3),
        "افزایش مجازات رهاسازی آب‌های آلوده": (2, 3, 3),
        "نصب کنتور هوشمند چاه‌های کشاورزی": (2, 3, 2),
        "مشوق برای مشترکان کم‌مصرف": (3, 2, 1)
    }

    choice = st.radio("یکی از لوایح را انتخاب کن:", list(bills.keys()))

    if st.button("ثبت انتخاب"):
        st.session_state.score = sum(bills[choice])
        st.session_state.stage = 2
        st.success("طرح انتخاب شد")

# -------------------------------
# مرحله ۲ – جمع‌آوری امضا
# -------------------------------
elif st.session_state.stage == 2:
    st.header("مرحله ۲: ثبت در هیئت رئیسه")

    features = [
        "تمرکز منطقه‌ای",
        "انضباط حزبی",
        "نفوذ سیاسی",
        "ریسک‌پذیری",
        "پایگاه اجتماعی"
    ]

    st.write("۵ گروه نماینده را انتخاب کن (حداقل ۳ سازگار):")
    selected = st.multiselect("گروه‌ها:", features)

    if st.button("بررسی امضاها"):
        if len(selected) >= 3:
            st.session_state.score += 5
            st.session_state.stage = 3
            st.success("امضاها جمع شد")
        else:
            st.error("امضا کافی نیست، بازی از ابتدا شروع می‌شود")
            st.session_state.stage = 1
            st.session_state.score = 0

# -------------------------------
# مرحله ۳ – کمیسیون تخصصی
# -------------------------------
elif st.session_state.stage == 3:
    st.header("مرحله ۳: کمیسیون تخصصی")

    commissions = [
        "کشاورزی، آب و منابع طبیعی",
        "برنامه و بودجه",
        "اقتصادی",
        "عمران",
        "انرژی"
    ]

    correct = "کشاورزی، آب و منابع طبیعی"
    choice = st.selectbox("کمیسیون مناسب را انتخاب کن:", commissions)

    if st.button("ثبت کمیسیون"):
        if choice == correct:
            st.session_state.score += 5
            st.success("انتخاب درست بود")
        else:
            st.warning("کمیسیون مرتبط نبود")

        st.session_state.stage = 4

# -------------------------------
# مرحله ۴ – صحن علنی (دور متوسط)
# -------------------------------
elif st.session_state.stage == 4:
    st.header("مرحله ۴: صحن علنی مجلس")

    pros = random.randint(4, 6)
    cons = random.randint(4, 6)

    st.write(f"نطق موافق: {pros}")
    st.write(f"نطق مخالف: {cons}")

    spend = st.slider(
        "امتیاز مصرفی برای خنثی‌سازی مخالفان:",
        0,
        st.session_state.score
    )

    if st.button("رأی‌گیری"):
        result = pros + spend - cons
        if result > 0:
            st.success("طرح تصویب شد 🎉")
            st.write("امتیاز نهایی:", st.session_state.score)
        else:
            st.error("طرح رأی نیاورد ❌")

        st.session_state.stage = 1
        st.session_state.score = 0
