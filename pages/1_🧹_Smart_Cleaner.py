import streamlit as st
import time

st.set_page_config(page_title="Smart Cleaner", page_icon="🧹", layout="wide")

st.title("🧹 Smart Cleaner")
st.markdown("สแกนหาไฟล์ขยะ ไฟล์ซ้ำซ้อน และไฟล์ขนาดใหญ่ที่ไม่ได้ใช้งาน เพื่อเคลียร์พื้นที่จัดเก็บอย่างปลอดภัย")

# Options
st.markdown("### ตัวเลือกการสแกน")
scan_temp = st.checkbox("🗑️ Temporary Files (ไฟล์ขยะของระบบ, Cache, Log Files)", value=True)
scan_dup = st.checkbox("📄 Duplicate Files (ไฟล์ที่ซ้ำซ้อนกันในหลายตำแหน่ง)", value=True)
scan_large = st.checkbox("📦 Large & Unused Files (ไฟล์ขนาดใหญ่ที่ไม่ได้เปิดนานกว่า 90 วัน)", value=False)

target_folder = st.text_input("โฟลเดอร์เป้าหมาย", value="C:\\Users\\admin")

if st.button("🔍 Scan Now", type="primary"):
    with st.spinner("กำลังสแกน..."):
        time.sleep(2)
        st.session_state['scan_done'] = True

if st.session_state.get('scan_done', False):
    st.success("สแกนเสร็จสิ้น! พบไฟล์ขยะและไฟล์ซ้ำซ้อนจำนวน 156 ไฟล์ (3.8 GB)")
    
    st.markdown("#### 🗑️ Temporary Files (1.2 GB)")
    st.code("C:\\Users\\admin\\AppData\\Local\\Temp\\AppCache_v2.tmp  - 256 MB\nC:\\Windows\\Temp\\system_log_2026.log - 180 MB", language="text")
    
    st.markdown("#### 📄 Duplicate Files (1.8 GB)")
    st.code("C:\\Users\\admin\\Pictures\\vacation_photo (2).jpg - 8.5 MB\nC:\\Users\\admin\\Documents\\report_final_v2_COPY.xlsx - 4.2 MB", language="text")
    
    if st.button("🗑️ Clean Up — เคลียร์ 3.8 GB"):
        with st.spinner("กำลังลบไฟล์..."):
            time.sleep(1.5)
            st.success("เคลียร์พื้นที่สำเร็จ! ได้พื้นที่คืน 3.8 GB")
            st.session_state['scan_done'] = False
            st.balloons()
