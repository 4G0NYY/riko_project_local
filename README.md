# Project Riko

Project Riko is a anime focused LLM project by Just Rayen. She listens, and remembers your conversations. It combines a local GPT4all model, GPT-SoVITS voice synthesis, and Faster-Whisper ASR into a fully configurable conversational pipeline.

**tested with python 3.10 Windows >10 and Linux Ubuntu**
## ✨ Features

- 💬 **LLM-based dialogue** using local GPT4all API (fully offline, no API keys required!)
- 🧠 **Conversation memory** to keep context during interactions
- 🔊 **Voice generation** via GPT-SoVITS API
- 🎧 **Speech recognition** using Faster-Whisper
- 📁 Clean YAML-based config for personality configuration
- 🚀 **100% Local** - no cloud dependencies!


## ⚙️ Configuration

All prompts and parameters are stored in `character_config.yaml`.

```yaml
# GPT4all API Configuration
gpt4all_api_url: http://localhost:4891/v1
history_file: chat_history.json
temperature: 0.7
max_tokens: 2048

presets:
  default:
    system_prompt: |
      You are a helpful assistant named Riko.
      You speak like a snarky anime girl.
      Always refer to the user as "senpai".

sovits_ping_config:
  text_lang: en
  prompt_lang : en
  ref_audio_path : D:\PyProjects\waifu_project\riko_project\character_files\main_sample.wav
  prompt_text : This is a sample voice for you to just get started with because it sounds kind of cute but just make sure this doesn't have long silences.
  
```

You can define personalities by modifying the config file.

**Note:** Make sure GPT4all is running on `localhost:4891` before starting the application!


## 🛠️ Setup

### Install Dependencies

```bash
pip install uv 
uv pip install -r extra-req.txt
uv pip install -r requirements.txt
```

**If you want to use GPU support for Faster whisper** Make sure you also have:

* CUDA & cuDNN installed correctly (for Faster-Whisper GPU support)
* `ffmpeg` installed (for audio processing)


## 🧪 Usage

### 1. Start GPT4all API Server

Make sure GPT4all is running locally with the API server enabled on port 4891:
```bash
gpt4all --listen 127.0.0.1:4891
```

### 2. Launch the GPT-SoVITS API 

(Follow GPT-SoVITS documentation to start the TTS server)

### 3. Run the main script:

```bash
python server/main_chat.py
```

The flow:

1. Riko listens to your voice via microphone (push to talk)
2. Transcribes it with Faster-Whisper
3. Passes it to local GPT4all (fully offline!)
4. Generates a response
5. Synthesizes Riko's voice using GPT-SoVITS
6. Plays the output back to you


## 📌 TODO / Future Improvements

* [ ] GUI or web interface
* [ ] Live microphone input support
* [ ] Emotion or tone control in speech synthesis
* [ ] VRM model frontend


## 🧑‍🎤 Credits

* Voice synthesis powered by [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
* ASR via [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)
* Local LLM via [GPT4all](https://github.com/nomic-ai/gpt4all)


## 📜 License

MIT — feel free to clone, modify, and build your own waifu voice companion.


