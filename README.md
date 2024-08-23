<p align="center">

  <h1 align="center"> 🎙️ AI Voice Assistance Pipeline</h1>
  <p align="center">
    An efficient pipeline for handling voice queries with low latency and high customization.
    <br />
    <br />
  </p>
</p>

Welcome to the **AI Voice Assistance Pipeline** project! This pipeline is designed to convert voice input to text, process it through a Large Language Model (LLM), and convert the generated text back into speech. ⚡

## 📝 Project Details

This project is an AI Voice Assistance Pipeline designed to handle voice queries by converting them into text, processing them through a Large Language Model (LLM), and converting the generated text back into speech. The pipeline is optimized for low latency and includes Voice Activity Detection (VAD), response length limitation, and adjustable parameters like pitch, voice gender, and speech speed.

### ✨ Features

- **Voice-to-Text Conversion**: Uses Whisper, an open-source Speech2Text model, to convert voice input into text. The model is configured for English with a 16 kHz sampling rate and mono audio.
- **Text Processing**: Integrates with a Hugging Face Transformers model to process text queries and generate concise responses.
- **Text-to-Speech Conversion**: Converts text back into speech using the Edge TTS API, allowing for customization of voice parameters such as type, rate, and pitch.

### 📂 Project Directory Structure

```plaintext
voice_assistant/
├── data/
│   └── (Contains input audio files)
├── output_files/
│   └── (Contains output audio files)
├── src/
│   ├── voice_to_text.py  # Handles conversion of voice input to text
│   ├── text_to_llm.py     # Processes the text input with a language model
│   ├── text_to_speech.py  # Converts text output from LLM to speech
│   └── main.py            # Main script that integrates all components
├── requirements.txt       # Lists all dependencies required for the project
└── README.md              # Documentation for the project
```

# 🚀 Setup Instructions

Make sure you have the following installed:

* Python 3.8+
* Pip
* Git

Follow these steps to set up the project on your local machine:

### Clone the Repository:

```bash
git clone https://github.com/VeeraVenkataKarthikBarrekala/voice_assistant.git
cd voice_assistant
```

### Create a Virtual Environment:

```bash
conda create -n env python=3.10 -y
conda activate env
```

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Download the spaCy language model:
```bash
python -m spacy download en_core_web_sm
```

### Run the pipeline:
Navigate to the src directory and run the main script:


```bash
cd src
python main.py
```

The script will prompt you to either use the microphone for live input or an audio file for pre-recorded input.


# 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

### Fork the Repository
Click the "Fork" button at the top-right corner of the repository page on GitHub.

### Clone Your Fork

```bash
git clone https://github.com/your-username/voice_assistant.git
cd voice_assistant
```

### Create a Branch
Create a new branch for your feature or bug fix:
```bash
git checkout -b feature-name
```

### Make Your Changes
Implement your feature or bug fix.

### Commit Your Changes

```bash
git add .
git commit -m "Describe your changes"
```

### Push to Your Fork

```bash
git push origin feature-name
```

### Submit a Pull Request
Go to the original repository on GitHub and click the "New Pull Request" button.


---

## Author

**Veera Venkata Karthik Barrekala**

- **LinkedIn**: [Veera Venkata Karthik Barrekala](https://www.linkedin.com/in/your-linkedin-profile/)

Feel free to connect with me on LinkedIn for any queries or further collaboration!



