# 🌿 Touch Grass Sports AI

**Open Source Offline AI** that pushes you outside through real sports challenges.

> "Stop scrolling. Touch grass. Move your body."

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Offline First](https://img.shields.io/badge/Offline-First-brightgreen.svg)](#)
[![Ollama Compatible](https://img.shields.io/badge/Ollama-Compatible-orange.svg)](https://ollama.com)
[![Multi-language](https://img.shields.io/badge/Language-EN%20%7C%20ID-blue.svg)](#)

A **100% offline** local AI that generates personalized outdoor sports challenges.  
No internet needed after setup. Full privacy. Open source.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **100% Offline** | Runs locally with Ollama or pure rule-based mode (no model required) |
| **Touch Grass Theme** | Every challenge must be done outdoors + includes touching grass/nature |
| **Multi-language** | Supports English and Indonesian (easily extensible) |
| **Personalization** | Fitness level, sport type, available time, location, and notes |
| **Two Interfaces** | Modern Web UI (Gradio) + lightweight CLI |
| **Two Engines** | Local LLM (Ollama) for creative challenges, or fast rule-based database |
| **Full Privacy** | No data is ever sent to the cloud |
| **Open Source** | MIT License — free to use, modify, and share |

---

## 🎯 Challenge Examples

**Beginner – Running**  
> Easy 1–1.5 km jog in the park → 15 jumping jacks on the grass → touch the grass with both hands.

**Intermediate – Basketball**  
> Play 20–30 minutes on outdoor court → 5 push-ups on the grass for every missed shot → cool down sitting on the grass.

**Advanced – Calisthenics**  
> 5 rounds of HIIT on the grass field (burpees, jump squats, sprints, explosive push-ups) → mountain climber + plank finisher.

---

## 🛠️ System Requirements

- **Python** 3.9 or higher
- **Ollama** (optional, recommended for best experience)
- Small local models (examples):
  - `llama3.2` (recommended)
  - `phi3`
  - `gemma2:2b`
  - `qwen2.5:3b`
- Minimum RAM: 4 GB (rule-based) / 8 GB+ (with model)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gabutersproject/touch-grass-sports-ai.git
cd touch-grass-sports-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. (Optional) Install & Setup Ollama

1. Download Ollama from [https://ollama.com](https://ollama.com)
2. Pull a small model:

```bash
ollama pull llama3.2
# or
ollama pull phi3
ollama pull gemma2:2b
```

### 4. Run the Application

**Web UI (recommended):**
```bash
python app.py
```
Open your browser → `http://localhost:7860`

**Rule-based only (no Ollama):**
```bash
python app.py --rule-based
```

**CLI:**
```bash
python cli.py --level Intermediate --sport "running" --time "40 minutes" --lang en
```

---

## 📖 How to Use

### Web Interface

1. Select **Language** (English / Indonesian)
2. Select **Fitness Level** (Beginner / Intermediate / Advanced)
3. Enter your preferred **Sport** (running, basketball, calisthenics, cycling, football, hiking, etc.)
4. (Optional) Fill in available time, location, and extra notes
5. Click **🚀 Generate Touch Grass Challenge**
6. Go outside and complete it!

### Command Line

```bash
python cli.py \
  --level Advanced \
  --sport "calisthenics" \
  --time "35 minutes" \
  --location "grass field" \
  --notes "full body focus" \
  --lang en \
  --model llama3.2
```

**Available arguments:**

| Argument | Default | Description |
|----------|---------|-------------|
| `--level` | Beginner | Beginner / Intermediate / Advanced |
| `--sport` | general | Preferred sport |
| `--time` | - | Available time |
| `--location` | - | Preferred location |
| `--notes` | - | Additional notes |
| `--lang` | en | Language: `en` (English) or `id` (Indonesian) |
| `--rule-based` | false | Force rule-based mode (no LLM) |
| `--model` | llama3.2 | Ollama model name |

---

## 🧠 How It Works

```
User Input (+ Language)
    ↓
Challenge Engine
  1. Is Ollama available?
  2. Yes → Generate with Local LLM + Prompt (in selected lang)
  3. No / Failed → Rule-based Database (in selected lang)
    ↓
Outdoor Challenge + Touch Grass Moment
```

The **System Prompt** is strictly designed so the AI:
- Always generates **outdoor** activities
- Includes a "touch grass / soil / nature" moment
- Stays realistic and safe for the user's level
- Provides time estimate + intensity
- Gives supportive but firm motivation
- Responds in the selected language

---

## 🌐 Multi-language Support

Currently supported:
- 🇬🇧 **English** (`en`)
- 🇮🇩 **Indonesian** (`id`)

The language affects:
- System prompt used by the LLM
- Rule-based challenge database
- UI labels (Web interface)

Adding a new language is straightforward — just extend the dictionaries in `prompts.py` and `challenges_db.py`.

---

## 📁 Project Structure

```
touch-grass-sports-ai/
├── app.py                 # Web UI (Gradio)
├── cli.py                 # Command Line Interface
├── challenge_engine.py    # Main challenge generation logic
├── challenges_db.py       # Rule-based challenge database (multi-lang)
├── prompts.py             # System prompts & templates (multi-lang)
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
└── README.md              # This documentation
```

---

## 🧩 Dependencies

```txt
gradio>=4.0.0
ollama>=0.3.0
pydantic>=2.0.0
```

---

## 🤝 Contributing

Contributions are very welcome! Some ideas:

- [ ] Daily progress & streak tracking
- [ ] More sports (outdoor swimming, climbing, trail running, etc.)
- [ ] Additional languages
- [ ] Voice input / Text-to-Speech
- [ ] Export challenges to Markdown / PDF / Calendar
- [ ] Automatic "Daily Challenge" mode
- [ ] Future integration with phone sensors (steps, GPS)

**How to contribute:**
1. Fork this repository
2. Create a new branch (`git checkout -b cool-feature`)
3. Commit your changes
4. Push and open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full details.

---

## 💡 Philosophy

Made for people who:

- Are tired of doomscrolling
- Want to move more in the real world
- Love sports but often feel lazy to go outside
- Believe that "touch grass" is the best medicine for an over-online brain

**Stop scrolling. Touch grass. Move your body.** 🏃‍♂️🌿

---

Made with 💚 for the outdoor movement.
