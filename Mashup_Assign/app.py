import streamlit as st
import os
import zipfile
import subprocess
import sys

st.set_page_config(page_title="Mashup Web Service")
st.title("🎵 Mashup Web Service")

singer = st.text_input("Singer Name", value="Karan Aujla")
n_videos = st.number_input("# of videos", min_value=1, value=25)
duration = st.number_input("duration of each video (sec)", min_value=1, value=25)
email_id = st.text_input("Email Id")

if st.button("Submit"):
    if not singer or not email_id or "@" not in email_id:
        st.error("Email id must be correct")
    elif n_videos <= 10 or duration <= 20:
        st.error("Constraints: N > 10 and Y > 20")
    else:
        with st.spinner("Processing... This may take 2-3 minutes."):
            output_mp3 = "result.mp3"
            output_zip = "result.zip"
            
            if os.path.exists(output_mp3): os.remove(output_mp3)
            if os.path.exists(output_zip): os.remove(output_zip)

            script_path = os.path.join(os.getcwd(), "102317138.py")
            process = subprocess.run([
                sys.executable, script_path, 
                singer, str(n_videos), str(duration), output_mp3
            ], capture_output=True, text=True)

            if os.path.exists(output_mp3):
                with zipfile.ZipFile(output_zip, 'w') as zipf:
                    zipf.write(output_mp3)
                
                st.success("Mashup Created Successfully!")
                with open(output_zip, "rb") as f:
                    st.download_button("Download Zip File", f, file_name=output_zip)
            else:
                st.error("Cloud Error: YouTube blocked the server (403).")
                with st.expander("Technical Log"):
                    st.code(process.stderr)