# 🎥 AI YouTube Video Summarizer

An **AI powered YouTube Video Summarizer** that converts long YouTube videos into concise, easy-to-understand summaries using **Generative AI and transformer based models**.

This project is designed to help students and learners quickly grasp key concepts from educational videos without watching the entire content.


## 📌 Problem Statement

Educational and technical YouTube videos are often long and time consuming.  
Students need a faster way to:
- Understand the core ideas of a video
- Revise content efficiently
- Extract meaningful insights from long-form videos

This project solves the problem by automatically summarizing YouTube video transcripts using AI.


## 🚀 Features

- 🔗 Accepts any valid YouTube video URL
- 📜 Extracts video transcripts automatically
- 🧠 Handles long videos using chunk-based processing
- 📝 Generates concise and readable summaries
- 🖥️ Simple and interactive Streamlit UI
- ⚠️ Graceful handling of videos without transcripts


## 🧠 System Architecture

1. User provides a YouTube video URL  
2. Transcript is fetched using YouTube Transcript API  
3. Text is cleaned and split into manageable chunks  
4. Each chunk is summarized using a transformer based model  
5. All summaries are merged into a final output  

This approach ensures efficient processing of long videos.


## 🛠️ Tech Stack

| Category | Tools |
|--------|------|
| Programming Language | Python |
| UI Framework | Streamlit |
| NLP Model | BART (facebook/bart large cnn) |
| AI Library | HuggingFace Transformers |
| Transcript API | youtube transcript api |




## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-youtube-summarizer.git
cd ai-youtube-summarizer


2️⃣ Create & Activate Virtual Environment
python -m venv venv
.\venv\Scripts\Activate.ps1


3️⃣ Install Dependencies
pip install -r requirements.txt







