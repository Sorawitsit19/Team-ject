import streamlit as st
import time

st.set_page_config(page_title="Auto Monitor", page_icon="👁️", layout="wide")

st.title("👁️ Auto Monitor — Watchdog")
st.markdown("ระบบเฝ้าระวังโฟลเดอร์อัตโนมัติ — สร้างกฏเพื่อจัดการไฟล์ใหม่ที่เข้ามาโดยไม่ต้องทำเอง")

# Active Rules
st.subheader("กฏที่ใช้งานอยู่ (Active Rules)")

rules = [
    {"name": "จัดเรียงไฟล์รูปภาพ", "folder": "C:\\Users\\admin\\Downloads", "cond": "เมื่อมีไฟล์ .jpg, .png, .heic", "action": "ย้ายไปที่ Pictures", "active": True},
    {"name": "แปลง Word เป็น PDF", "folder": "C:\\Users\\admin\\Documents", "cond": "เมื่อมีไฟล์ .docx", "action": "แปลงเป็น PDF", "active": True},
    {"name": "จัดเรียงไฟล์วิดีโอ", "folder": "C:\\Users\\admin\\Downloads", "cond": "เมื่อมีไฟล์ .mp4, .avi, .mov", "action": "ย้ายไปที่ Videos", "active": False},
]

for r in rules:
    with st.container():
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            st.toggle("เปิด/ปิด", value=r["active"], key=r["name"])
        with col2:
            st.markdown(f"**{r['name']}**")
            st.caption(f"📁 {r['folder']} ➡️ {r['cond']} ➡️ {r['action']}")
        st.divider()

# New Rule
with st.expander("✨ สร้างกฏใหม่"):
    st.text_input("ชื่อกฏ", placeholder="เช่น จัดเรียงไฟล์ PDF")
    st.text_input("โฟลเดอร์เป้าหมาย", placeholder="C:\\Users\\admin\\Downloads")
    st.selectbox("เงื่อนไข", ["เมื่อมีไฟล์รูปภาพใหม่", "เมื่อมีไฟล์เอกสารใหม่", "เมื่อมีไฟล์วิดีโอใหม่", "เมื่อมีไฟล์บีบอัดใหม่"])
    st.selectbox("การกระทำ", ["ย้ายไปที่โฟลเดอร์...", "แปลงเป็น PDF ทันที", "แปลงเป็น JPG ทันที", "บีบอัดไฟล์"])
    if st.button("บันทึกกฏใหม่", type="primary"):
        st.success("สร้างกฏสำเร็จ!")

# Activity Log
st.subheader("📋 Activity Log")
log_text = """[08:31:15] MOVE   vacation_photo_001.jpg → C:\\Users\\admin\\Pictures
[08:30:42] CONVERT report_draft.docx → report_draft.pdf
[08:28:10] MOVE   screenshot_2026.png → C:\\Users\\admin\\Pictures
[08:25:33] MOVE   landscape.heic → C:\\Users\\admin\\Pictures"""

st.code(log_text, language="text")
if st.button("เคลียร์ Log"):
    st.info("Log ถูกเคลียร์แล้ว")
