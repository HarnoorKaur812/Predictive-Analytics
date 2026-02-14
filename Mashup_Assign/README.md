This project was developed as part of the Predictive Analytics (TIET) assignment. It is designed to automatically generate an audio mashup by collecting multiple YouTube songs of a given singer and merging them into one MP3 file.

The implementation is divided into two parts. The first program (102317138.py) works as a command-line tool that downloads audio using yt-dlp, trims the required duration using pydub, and then joins all clips into a single mashup. The second program (app.py) provides a simple web interface using Streamlit, where the user can enter input values and download the final output as a ZIP file.

Inputs: Singer name, number of videos, duration per video, and email ID.
Output: A mashup MP3 file packed inside a ZIP archive.

Live App Link : [Link](https://mashupassign-umrenhshbhrdapp6g7ygzrp.streamlit.app/)
