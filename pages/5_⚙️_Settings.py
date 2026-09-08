import streamlit as st

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="wide")

st.title("⚙️ Settings")
st.markdown("ตั้งค่าระบบและการเชื่อมต่อ API")

with st.container():
    st.subheader("🔑 API Configuration")
    st.caption("ตั้งค่า Google Gemini API สำหรับฟีเจอร์ AI Vision")
    st.text_input("Google Gemini API Key", type="password", value="AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    if st.button("บันทึก API Key"):
        st.success("บันทึก API Key สำเร็จ! พร้อมใช้งาน")

st.divider()

with st.container():
    st.subheader("📁 Default Output Folder")
    st.caption("โฟลเดอร์เริ่มต้นสำหรับบันทึกไฟล์ที่แปลงแล้ว")
    st.text_input("เส้นทางโฟลเดอร์", value="C:\\Users\\admin\\Documents\\ZipZap_Output")
    
st.divider()

with st.container():
    st.subheader("🚀 Startup & Background")
    st.checkbox("เริ่มต้นพร้อมระบบ (เปิดโปรแกรมอัตโนมัติเมื่อเปิดเครื่อง)", value=False)
    st.checkbox("ทำงานเบื้องหลัง (System Tray)", value=True)
    st.checkbox("เสียงแจ้งเตือน", value=True)

st.divider()

with st.container():
    st.subheader("ℹ️ About ZipZap")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**เวอร์ชัน:** 2.0.0")
        st.markdown("**พัฒนาโดย:** ทีมเจ็ค")
    with col2:
        st.markdown("**สร้างด้วย:** Streamlit (Python 100%)")
        st.markdown("**AI Engine:** Google Gemini API")
