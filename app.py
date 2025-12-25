import streamlit as st
import random

st.set_page_config(page_title="Parliament Game", layout="centered")

st.title("?? »«“Ì ﬁ«‰Ê‰ùê–«—Ì Å«—·„«‰")

if "stage" not in st.session_state:
    st.session_state.stage = 1
    st.session_state.score = 0

# -------------------------------
# „—Õ·Â ? ñ «‰ Œ«» ÿ—Õ
# -------------------------------
if st.session_state.stage == 1:
    st.header("„—Õ·Â ?: «‰ Œ«» ÿ—Õ")

    bills = {
        "«›“«Ì‘ ⁄Ê«—÷ „Õ’Ê·«  Å—¬» ’«œ—« Ì": (3, 3, 3),
        "«›“«Ì‘ „Ã«“«  —Â«”«“Ì ¬»ùÂ«Ì ¬·ÊœÂ": (2, 3, 3),
        "‰’» ò‰ Ê— ÂÊ‘„‰œ ç«ÂùÂ«Ì ò‘«Ê—“Ì": (2, 3, 2),
        "„‘Êﬁ »—«Ì „‘ —ò«‰ ò„ù„’—›": (3, 2, 1)
    }

    choice = st.radio("ÌòÌ «“ ·Ê«ÌÕ —« «‰ Œ«» ò‰:", list(bills.keys()))

    if st.button("À»  «‰ Œ«»"):
        st.session_state.score = sum(bills[choice])
        st.session_state.stage = 2
        st.success("ÿ—Õ «‰ Œ«» ‘œ")

# -------------------------------
# „—Õ·Â ? ñ Ã„⁄ù¬Ê—Ì «„÷«
# -------------------------------
elif st.session_state.stage == 2:
    st.header("„—Õ·Â ?: À»  œ— ÂÌ∆  —∆Ì”Â")

    features = [
        " „—ò“ „‰ÿﬁÂù«Ì",
        "«‰÷»«ÿ Õ“»Ì",
        "‰›Ê– ”Ì«”Ì",
        "—Ì”òùÅ–Ì—Ì",
        "Å«Ìê«Â «Ã „«⁄Ì"
    ]

    st.write("? ê—ÊÂ ‰„«Ì‰œÂ —« «‰ Œ«» ò‰ (Õœ«ﬁ· ? ”«“ê«—):")
    selected = st.multiselect("ê—ÊÂùÂ«:", features)

    if st.button("»——”Ì «„÷«Â«"):
        if len(selected) >= 3:
            st.session_state.score += 5
            st.session_state.stage = 3
            st.success("«„÷«Â« Ã„⁄ ‘œ")
        else:
            st.error("«„÷« ò«›Ì ‰Ì” ° »«“Ì «“ «» œ« ‘—Ê⁄ „Ìù‘Êœ")
            st.session_state.stage = 1
            st.session_state.score = 0

# -------------------------------
# „—Õ·Â ? ñ ò„Ì”ÌÊ‰  Œ’’Ì
# -------------------------------
elif st.session_state.stage == 3:
    st.header("„—Õ·Â ?: ò„Ì”ÌÊ‰  Œ’’Ì")

    commissions = [
        "ò‘«Ê—“Ì° ¬» Ê „‰«»⁄ ÿ»Ì⁄Ì",
        "»—‰«„Â Ê »ÊœÃÂ",
        "«ﬁ ’«œÌ",
        "⁄„—«‰",
        "«‰—éÌ"
    ]

    correct = "ò‘«Ê—“Ì° ¬» Ê „‰«»⁄ ÿ»Ì⁄Ì"
    choice = st.selectbox("ò„Ì”ÌÊ‰ „‰«”» —« «‰ Œ«» ò‰:", commissions)

    if st.button("À»  ò„Ì”ÌÊ‰"):
        if choice == correct:
            st.session_state.score += 5
            st.success("«‰ Œ«» œ—”  »Êœ")
        else:
            st.warning("ò„Ì”ÌÊ‰ „— »ÿ ‰»Êœ")

        st.session_state.stage = 4

# -------------------------------
# „—Õ·Â ? ñ ’Õ‰ ⁄·‰Ì (œÊ— „ Ê”ÿ)
# -------------------------------
elif st.session_state.stage == 4:
    st.header("„—Õ·Â ?: ’Õ‰ ⁄·‰Ì „Ã·”")

    pros = random.randint(4, 6)
    cons = random.randint(4, 6)

    st.write(f"‰ÿﬁ „Ê«›ﬁ: {pros}")
    st.write(f"‰ÿﬁ „Œ«·›: {cons}")

    spend = st.slider(
        "«„ Ì«“ „’—›Ì »—«Ì Œ‰ÀÌù”«“Ì „Œ«·›«‰:",
        0,
        st.session_state.score
    )

    if st.button("—√ÌùêÌ—Ì"):
        result = pros + spend - cons
        if result > 0:
            st.success("ÿ—Õ  ’ÊÌ» ‘œ ??")
            st.write("«„ Ì«“ ‰Â«ÌÌ:", st.session_state.score)
        else:
            st.error("ÿ—Õ —√Ì ‰Ì«Ê—œ ?")

        st.session_state.stage = 1
        st.session_state.score = 0
