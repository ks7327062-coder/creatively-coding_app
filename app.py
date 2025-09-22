import streamlit as st
import os

# -------- PAGE CONFIG --------
st.set_page_config(page_title="🌑 Creatively Coding | إبداعيًا في البرمجة", layout="wide")

# -------- CUSTOM CSS --------
st.markdown("""
<style>
/* Gradient dark background */
.stApp {
    background: linear-gradient(120deg, #0f0c29, #302b63, #24243e);
    color: #f5f5f5;
    font-family: 'Segoe UI', sans-serif;
}

/* Header Title Gradient */
h1 {
    font-size: 52px;
    font-weight: bold;
    background: linear-gradient(90deg, #00d4ff, #ff00ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1e1e1e;
    color: #f5f5f5;
    font-size: 18px;
}

/* Video card */
.video-card {
    background-color: rgba(31,31,31,0.9);
    padding: 20px;
    margin: 15px 0;
    border-radius: 20px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.7);
    transition: transform 0.3s, box-shadow 0.3s;
}
.video-card:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.8);
}

/* Expander */
.streamlit-expanderHeader {
    color: #00d4ff;
    font-weight: bold;
}

/* Tabs */
.stTabs [role="tab"] {
    color: #00d4ff;
    font-weight: bold;
}

/* Footer */
.footer {
    text-align:center;
    padding:20px;
    font-size:14px;
    color: #aaa;
    border-top: 1px solid #333;
    margin-top:30px;
}
.footer a {
    color:#00d4ff;
    text-decoration:none;
}
.footer a:hover {
    text-decoration:underline;
}

/* About page profiles */
.profile-card {
    background-color: rgba(31,31,31,0.9);
    padding: 25px;
    margin: 15px;
    border-radius: 20px;
    text-align:center;
    box-shadow: 0 6px 16px rgba(0,0,0,0.7);
}
.profile-name {
    color:#00d4ff;
    font-weight:bold;
    font-size:22px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #00d4ff, #ff00ff);
    color: #fff;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 15px;
    border: none;
    transition: transform 0.2s, box-shadow 0.2s;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(0,0,0,0.6);
}
</style>
""", unsafe_allow_html=True)

# -------- SIDEBAR --------
page = st.sidebar.radio("📑 Navigate | الانتقال",
                        ["🏠 Home | الصفحة الرئيسية",
                         "🎓 Courses | الدورات",
                         "👤 About Us | عنا"])

# -------- HELPER FUNCTIONS --------
def load_videos_from_folder(folder_path):
    videos = {}
    if os.path.exists(folder_path):
        for file in sorted(os.listdir(folder_path)):
            if file.endswith(('.mp4', '.webm', '.mov')):
                title = os.path.splitext(file)[0].replace("_", " ").title()
                videos[title] = os.path.join(folder_path, file)
    return videos

def display_videos(videos_dict):
    cols = st.columns(2)
    i = 0
    for title, path in videos_dict.items():
        with cols[i % 2]:
            st.markdown(f'<div class="video-card"><h4>🎬 {title}</h4></div>', unsafe_allow_html=True)
            st.video(path)
            with st.expander("📖 Description | الوصف"):
                st.write("Add a description here for this video | أضف وصفًا لهذا الفيديو هنا.")
        i += 1

# -------- PAGE CONTENT --------
if page == "🏠 Home | الصفحة الرئيسية":
    st.markdown('<h1>🌑 Creatively Coding | إبداعيًا في البرمجة</h1>', unsafe_allow_html=True)
    st.write("منصة تعليمية تفاعلية تساعد الشعب اللبناني على تعلم البرمجة، الروبوتات، Scratch و Canva.")
    st.write("An interactive educational platform to help the Lebanese people learn Programming, Robotics, Scratch & Canva creatively.")

    # Buttons to navigate
    if st.button("🎓 Explore Courses | استكشف الدورات"):
        page = "🎓 Courses | الدورات"
    if st.button("👤 About Us | عنا"):
        page = "👤 About Us | عنا"

elif page == "🎓 Courses | الدورات":
    st.markdown('<h1>🎓 Courses | الدورات</h1>', unsafe_allow_html=True)
    st.write("اختر تصنيفاً لاستكشاف الدروس | Choose a category to explore lessons:")
    tabs = st.tabs(["🐍 Python", "🤖 Robotics", "🎮 Scratch", "🎨 Canva"])
    folders = {
        "🐍 Python": "videos/python",
        "🤖 Robotics": "videos/robotics",
        "🎮 Scratch": "videos/scratch",
        "🎨 Canva": "videos/canva"
    }
    for tab, category in zip(tabs, folders.keys()):
        with tab:
            videos = load_videos_from_folder(folders[category])
            if videos:
                display_videos(videos)
            else:
                st.info("No videos found! Please add videos to the folder | لم يتم العثور على أي فيديوهات!")

elif page == "👤 About Us | عنا":
    st.markdown('<h1>👤 About Us | عنا</h1>', unsafe_allow_html=True)
    st.write("مرحباً! نحن خليل شهاب وثلفيقار. نحب تعليم البرمجة والروبوتات والتصميم الرقمي.")
    st.write("Hi! We are Khalil Shehab and Thulfikar. We love teaching programming, robotics, and digital design.")
    st.write("هذه المنصة مخصصة لمساعدة الشعب اللبناني على التعلم بطريقة تفاعلية وممتعة.")
    st.write("This platform is designed to help the Lebanese people learn interactively and enjoyably.")

    cols = st.columns(2)
    with cols[0]:
        st.markdown('<div class="profile-card"><p class="profile-name">خليل شهاب</p><p>👨‍💻 Programming & Robotics</p></div>', unsafe_allow_html=True)
    with cols[1]:
        st.markdown('<div class="profile-card"><p class="profile-name">ثلفيقار</p><p>🎨 Digital Design & Scratch</p></div>', unsafe_allow_html=True)

    st.markdown("**Contact us | للتواصل معنا:**\n"
                "- 📧 Email: ks3727062@gmail.com\n"
                "- 🌐 Website: 🌑 Creatively Coding | إبداعيًا في البرمجة\n"
                "- 💬 Instagram/Twitter: @creativelycoding")

# -------- FOOTER --------
st.markdown(f"""
<div class="footer">
<p>© 2025 خليل شهاب & ثلفيقار | Made with ❤️ for the Lebanese people 🇱🇧 — 
Contact: <a href="mailto:ks3727062@gmail.com">ks3727062@gmail.com</a></p>
</div>
""", unsafe_allow_html=True)
