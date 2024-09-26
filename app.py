import streamlit as st

# Centered title of the Streamlit app with emoji
st.markdown("<h1 style='text-align: center;'>🎾 Build an AI/ML Tennis Analysis System with YOLO, PyTorch, and Key Point Extraction 🎥</h1>", unsafe_allow_html=True)

# Add a subheading and description
st.markdown("""
    Welcome to the **Tennis Analysis System**! This app showcases the comparison between the original input video and the processed output video using advanced AI/ML techniques for player movement analysis.
""")

# Styling for input video section
st.markdown("### 🎬 **Input Video (Before Analysis)**")
st.markdown("Here's the original footage before any processing:")

# Display the input video
input_video_file = open('input_videos/input_video(DEMO).mp4', 'rb')  # Replace with the path to your input video
input_video_bytes = input_video_file.read()
st.video(input_video_bytes)

# Separator for better styling
st.markdown("---")

# Styling for output video section
st.markdown("### 🛠️ **Output Video (After Analysis)**")
st.markdown("Here’s the video after applying AI/ML analysis for detecting key points and movements:")

# Display the output video
output_video_file = open('output_videos/output_video(DEMO).mp4', 'rb')  # Replace with the path to your output video
output_video_bytes = output_video_file.read()
st.video(output_video_bytes)

# Add a separator line
st.markdown("---")

# Add a gallery section for images before and after
st.markdown("### 📸 **Gallery: Before and After Analysis**")
st.markdown("Here are some images showcasing the analysis process:")

# Display before and after images
col1, col2 = st.columns(2)  # Create two columns for the gallery

# Display before and after images
with col1:
    st.image('input_videos/image.png', caption='Before Analysis', use_column_width=True)  # Replace with your image path

with col2:
    st.image('output_videos/screenshot.jpeg', caption='After Analysis', use_column_width=True)  # Replace with your image path

# Add a black card with YOLO description using custom HTML and inline CSS
st.markdown("""
            <hr>
<div style="background-color:black;padding:10px;border-radius:10px;">
    <h3 style="color:white;text-align:center;">🖥️ How YOLO Works in Tennis Analysis</h3>
    <ul style="color:white;">
        <li>🔍 <strong>Object Detection</strong>: YOLO (You Only Look Once) detects players and objects in the tennis video in real-time.</li>
        <li>🧠 <strong>Key Point Extraction</strong>: YOLO identifies crucial points such as player movements, racket position, and ball trajectory.</li>
        <li>⚡ <strong>Real-Time Processing</strong>: YOLO is highly efficient, allowing quick detection and tracking of player actions frame-by-frame.</li>
        <li>🎯 <strong>Accuracy & Speed</strong>: YOLO combines speed with high accuracy, making it ideal for fast-paced sports like tennis.</li>
    </ul>
    <p style="color:white;text-align:center;">🚀 YOLO plays a vital role in enhancing performance analysis by providing detailed insights into player movements and game strategy.</p>
</div>
""", unsafe_allow_html=True)

# Add a new section for additional images with a different header
st.markdown("---")
st.markdown("### 🖼️ **Additional Analysis Sections**")
st.markdown("Below are some additional images showcasing different aspects of the tennis analysis:")

# Create columns for additional images
col1, col2, col3 = st.columns(3)  # Create three columns for the new images

# Assuming you have additional images saved in 'images/section1.jpg', 'images/section2.jpg', and 'images/section3.jpg'
with col1:
    st.image('Minor Images/display.PNG', caption='Section Analysis 1', use_column_width=True)  # Replace with your image path

with col2:
    st.image('Minor Images/image.png', caption='Section Analysis 2', use_column_width=True)  # Replace with your image path

with col3:
    st.image('Minor Images/Finding and Describig each Box and their role.PNG', caption='Describing and Analysis Per ID^s', use_column_width=True)  # Replace with your image path

with col1:
    st.image('Minor Images/Variation and Tracking Object.PNG', caption='Variation & Tracking Ball The Object', use_column_width=True)  # Replace with your image path

with col2:
    st.image('Minor Images/Final Output Videos.jpeg', caption='Final Output', use_column_width=True)  # Replace with your image path

# Add a footer or credits section with emojis in bold, italic, and centered
st.markdown("""
            <hr>
<div style="text-align:center; font-weight:bold; font-style:italic;">
    ---
    Made with ❤️ by Dhruv Dhayal | 🚀 Powered by AI/ML & Streamlit
</div>
""", unsafe_allow_html=True)
