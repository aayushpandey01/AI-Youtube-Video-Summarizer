import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import nltk
import re

nltk.download('punkt')

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="AI YouTube Video Summarizer", layout="wide")
st.title("AI YouTube Video Summarizer")
st.write("Paste a YouTube video link to generate an AI-powered summary")

# -------------------- FUNCTIONS --------------------

def extract_video_id(url):
    """
    Extracts YouTube video ID from different URL formats
    """
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None


def get_transcript(video_id):
    """
    Fetches transcript using stable YouTubeTranscriptApi method
    """
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([item["text"] for item in transcript])
    return full_text


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\[.*?\]", "", text)
    return text


def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks


def load_summarizer():
    return pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )


def summarize_chunks(chunks, summarizer):
    summaries = []
    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=130,
            min_length=40,
            do_sample=False
        )
        summaries.append(summary[0]["summary_text"])
    return summaries


# -------------------- UI --------------------

youtube_url = st.text_input("Enter YouTube Video URL")

if st.button("Generate Summary"):
    if not youtube_url:
        st.warning("Please enter a YouTube URL")
    else:
        with st.spinner("Processing video..."):
            try:
                video_id = extract_video_id(youtube_url)

                if not video_id:
                    st.error("Invalid YouTube URL")
                    st.stop()

                transcript_text = get_transcript(video_id)
                cleaned_text = clean_text(transcript_text)
                chunks = chunk_text(cleaned_text)

                summarizer = load_summarizer()
                summaries = summarize_chunks(chunks, summarizer)

                final_summary = " ".join(summaries)

                st.success("Summary Generated!")
                st.subheader("Video Summary")
                st.write(final_summary)

            except Exception as e:
                st.error("Unable to process this video.")
                st.info(
                    "Possible reasons:\n"
                    "- Captions are disabled\n"
                    "- Video is private\n"
                    "- Transcript not available"
                )

