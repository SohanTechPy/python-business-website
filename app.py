import streamlit as st

# 1. पेज का सेटअप (Professional & Wide Layout)
st.set_page_config(
    page_title="Apex Digital | Grow Your Business", 
    page_icon="💼", 
    layout="wide"
)

# 2. नेविगेशन मेन्यू (Navigation Menu)
st.sidebar.title("🚀 Apex Digital")
page = st.sidebar.radio("Go to:", ["Home", "Our Services", "Contact Us"])

# --- PAGE 1: HOME ---
if page == "Home":
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>We Build Digital Solutions For Your Business</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #4B5563;'>हम आपके बिजनेस को ऑनलाइन ले जाने में मदद करते हैं</h3>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎯 हमारा उद्देश्य")
        st.write("हम छोटे और बड़े व्यवसायों के लिए आधुनिक, तेज़ और सुरक्षित वेबसाइट्स और ऐप्स बनाते हैं ताकि वे अपनी सेल्स को 10x बढ़ा सकें।")
    with col2:
        st.subheader("💡 हमें क्यों चुनें?")
        st.write("✓ 100% रिस्पॉन्सिव डिज़ाइन\n\n✓ बेहतरीन परफॉरमेंस\n\n✓ 24/7 सपोर्ट")

# --- PAGE 2: SERVICES ---
elif page == "Our Services":
    st.markdown("<h2 style='color: #1E3A8A;'>🛠️ हमारी सर्विसेज</h2>", unsafe_allow_html=True)
    st.write("हम आपके बिजनेस की ज़रूरतों के हिसाब से बेस्ट सर्विस देते हैं:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### 🌐 Web Development\n\nआपके बिजनेस के लिए सुंदर और तेज़ वेबसाइट्स।")
    with col2:
        st.success("### 📱 App Development\n\nAndroid और iOS के लिए कस्टम मोबाइल ऐप्स।")
    with col3:
        st.warning("### 📈 Digital Marketing\n\nSEO और सोशल मीडिया के ज़रिए ग्राहकों तक पहुँचें।")

# --- PAGE 3: CONTACT US ---
elif page == "Contact Us":
    st.markdown("<h2 style='color: #1E3A8A;'>📞 हमसे संपर्क करें</h2>", unsafe_allow_html=True)
    st.write("अगर आप अपने बिजनेस के लिए वेबसाइट बनवाना चाहते हैं, तो नीचे दिया गया फॉर्म भरें:")
    
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("आपका नाम (Name):")
        email = st.text_input("आपका ईमेल (Email):")
        message = st.text_area("आपकी जरूरत (Message):")
        
        submit_button = st.form_submit_button("Submit Request 🚀")
        
        if submit_button:
            if name and email and message:
                st.success(f"थैंक यू {name}! आपकी रिक्वेस्ट हमारे पास पहुँच गई है। हम जल्द ही आपसे संपर्क करेंगे।")
            else:
                st.error("कृपया सभी फील्ड्स को भरें!")