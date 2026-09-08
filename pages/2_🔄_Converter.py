import streamlit as st
import time

st.set_page_config(page_title="Universal Converter", page_icon="🔄", layout="wide")

st.title("🔄 Universal Converter")
st.markdown("All-in-One แปลงไฟล์ทุกประเภท (เอกสาร, รูปภาพ, วิดีโอ/เสียง)")

tab1, tab2, tab3 = st.tabs(["📄 Document", "🖼️ Image", "🎬 Media"])

with tab1:
    st.subheader("แปลงไฟล์เอกสาร")
    st.file_uploader("ลากไฟล์เอกสารมาวางตรงนี้ (.docx, .doc)", accept_multiple_files=True, key="doc_up")
    st.selectbox("รูปแบบไฟล์ปลายทาง", ["PDF (.pdf)", "Text (.txt)"], key="doc_format")
    if st.button("เริ่มแปลงไฟล์เอกสาร", type="primary"):
        with st.spinner("กำลังแปลงไฟล์..."):
            time.sleep(2)
            st.success("แปลงไฟล์เอกสารเสร็จสมบูรณ์!")

with tab2:
    st.subheader("แปลงไฟล์รูปภาพ")
    st.file_uploader("ลากไฟล์รูปภาพมาวางตรงนี้ (.heic, .jpg, .png)", accept_multiple_files=True, key="img_up")
    
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("รูปแบบปลายทาง", ["JPEG (.jpg)", "PNG (.png)", "WebP (.webp)"], key="img_format")
    with col2:
        st.slider("คุณภาพ (Quality)", 10, 100, 85)
        
    if st.button("เริ่มแปลงไฟล์รูปภาพ", type="primary"):
        with st.spinner("กำลังแปลงไฟล์..."):
            time.sleep(2)
            st.success("แปลงไฟล์รูปภาพเสร็จสมบูรณ์!")

with tab3:
    st.subheader("แปลงไฟล์มีเดีย (Video & Audio)")
    st.file_uploader("ลากไฟล์วิดีโอ/เสียงมาวางตรงนี้ (.mp4, .avi, .mp3)", accept_multiple_files=True, key="media_up")
    
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("รูปแบบไฟล์ปลายทาง", ["MP3 (.mp3)", "WAV (.wav)", "MP4 (.mp4)"], key="media_format")
    with col2:
        st.selectbox("คุณภาพวิดีโอ", ["สูง (1080p)", "ปานกลาง (720p)", "ต่ำ (480p)"])
        
    if st.button("เริ่มแปลงไฟล์มีเดีย", type="primary"):
        with st.spinner("กำลังแปลงไฟล์..."):
            time.sleep(2)
            st.success("แปลงไฟล์มีเดียเสร็จสมบูรณ์!")
