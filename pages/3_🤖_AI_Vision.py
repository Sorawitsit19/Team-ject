import streamlit as st
import time

st.set_page_config(page_title="AI Vision", page_icon="🤖", layout="wide")

st.title("🤖 AI Vision — Gemini")
st.markdown("วิเคราะห์รูปภาพ ดึงข้อความ แยกประเภทภาพ และดึงจานสีด้วย Google Gemini AI")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("อัปโหลดรูปภาพ")
    img_file = st.file_uploader("รองรับ JPG, PNG, HEIC, WebP (สูงสุด 20MB)", type=["jpg", "png", "jpeg", "heic", "webp"])
    if img_file is not None:
        st.image(img_file, caption="ภาพที่คุณอัปโหลด", use_column_width=True)
        st.session_state['has_image'] = True
    else:
        st.session_state['has_image'] = False

with col2:
    st.subheader("คำสั่ง AI")
    
    prompt = st.text_input("พิมพ์คำถามของคุณ...", placeholder="เช่น อธิบายภาพนี้ให้ฟังหน่อย หรือดึงข้อความในภาพออกมา")
    
    st.markdown("**หรือเลือกคำสั่งด่วน:**")
    c1, c2 = st.columns(2)
    if c1.button("💬 อธิบายภาพนี้", use_container_width=True):
        prompt = "อธิบายภาพนี้"
    if c2.button("📝 ดึงข้อความ (OCR)", use_container_width=True):
        prompt = "ดึงข้อความ (OCR)"
    if c1.button("🏷️ แยกประเภทภาพ", use_container_width=True):
        prompt = "แยกประเภทภาพ"
    if c2.button("🎨 วิเคราะห์สีในภาพ", use_container_width=True):
        prompt = "วิเคราะห์สีในภาพ"
        
    if st.button("ส่งคำสั่งให้ AI 🚀", type="primary", use_container_width=True):
        if not st.session_state.get('has_image', False):
            st.error("กรุณาอัปโหลดรูปภาพก่อนส่งคำสั่งครับ")
        elif not prompt:
            st.warning("กรุณาระบุคำถามหรือเลือกคำสั่งด่วนครับ")
        else:
            with st.spinner("Gemini กำลังวิเคราะห์..."):
                time.sleep(2)
                st.success("วิเคราะห์เสร็จสมบูรณ์")
                
                # Mockup Response
                st.markdown("### ผลลัพธ์จาก AI:")
                if "อธิบาย" in prompt:
                    st.info("ภาพนี้แสดงทิวทัศน์ธรรมชาติที่สวยงาม มีภูเขาสูงเป็นฉากหลัง ท้องฟ้าสีครามกว้างใหญ่ องค์ประกอบหลักคือภูเขา ท้องฟ้า และทุ่งหญ้าสีเขียว")
                elif "OCR" in prompt or "ดึงข้อความ" in prompt:
                    st.info('พบข้อความ: "Welcome to ZipZap Smart File Manager"')
                elif "ประเภท" in prompt:
                    st.info("หมวดหมู่หลัก: Nature / Landscape\nTags: #nature #landscape #mountain")
                elif "สี" in prompt:
                    st.info("สีหลักในภาพ:\n1. 🟢 #4CAF50 — เขียวธรรมชาติ (35%)\n2. 🔵 #2196F3 — ฟ้าท้องฟ้า (28%)")
                else:
                    st.info(f"จากการวิเคราะห์ตามคำสั่ง '{prompt}' พบว่าภาพนี้มีลักษณะที่น่าสนใจหลายประการ (Mockup Response)")
