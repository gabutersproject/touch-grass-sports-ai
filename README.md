# 🌿 Touch Grass Sports AI

**Open Source Offline AI** that pushes you outside through real sports challenges.  
**Open Source Offline AI** yang mendorongmu keluar rumah lewat tantangan olahraga nyata.

> "Stop scrolling. Touch grass. Move your body."

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Offline First](https://img.shields.io/badge/Offline-First-brightgreen.svg)](#)
[![Ollama Compatible](https://img.shields.io/badge/Ollama-Compatible-orange.svg)](https://ollama.com)

A **100% offline** local AI that generates personalized outdoor sports challenges.  
No internet needed after setup. Full privacy. Open source.

Aplikasi AI lokal **100% offline** yang menghasilkan tantangan olahraga outdoor personal.  
Tidak butuh internet setelah setup. Privasi penuh. Open source.

---

## ✨ Features / Fitur Utama

| Feature / Fitur | Description (EN) | Deskripsi (ID) |
|-----------------|------------------|----------------|
| **100% Offline** | Runs locally with Ollama or pure rule-based mode | Berjalan lokal pakai Ollama atau mode rule-based tanpa model |
| **Touch Grass Theme** | Every challenge must be done outdoors + includes touching grass/nature | Setiap tantangan wajib outdoor + elemen menyentuh rumput/alam |
| **Personalization** | Fitness level, sport type, available time, location, notes | Level kebugaran, jenis olahraga, waktu, lokasi, catatan |
| **Two Interfaces** | Modern Web UI (Gradio) + lightweight CLI | Web UI modern (Gradio) + CLI ringan |
| **Two Engines** | Local LLM (Ollama) for creative challenges, or fast rule-based DB | Local LLM (Ollama) atau database rule-based yang cepat |
| **Full Privacy** | No data is ever sent to the cloud | Tidak ada data yang dikirim ke cloud |
| **Open Source** | MIT License — free to use, modify, and share | MIT License — bebas dipakai, dimodifikasi, dan dibagikan |

---

## 🎯 Challenge Examples / Contoh Tantangan

**Beginner – Running / Pemula – Lari**  
> Easy 1–1.5 km jog in the park → 15 jumping jacks on the grass → touch the grass with both hands.

**Intermediate – Basketball / Intermediate – Basket**  
> Play 20–30 minutes on outdoor court → 5 push-ups on the grass for every missed shot → cool down sitting on the grass.

**Advanced – Calisthenics / Advanced – Calisthenics**  
> 5 rounds of HIIT on the grass field (burpees, jump squats, sprints, explosive push-ups) → mountain climber + plank finisher.

---

## 🛠️ System Requirements / Persyaratan Sistem

- **Python** 3.9 or higher
- **Ollama** (optional, recommended for best experience)
- Small local models (examples):
  - `llama3.2` (recommended)
  - `phi3`
  - `gemma2:2b`
  - `qwen2.5:3b`
- Minimum RAM: 4 GB (rule-based) / 8 GB+ (with model)

---

## 🚀 Installation / Instalasi

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
python cli.py --level Intermediate --sport "running" --time "40 minutes"
```

---

## 📖 How to Use / Cara Penggunaan

### Web Interface

1. Select **Fitness Level** (Beginner / Intermediate / Advanced)
2. Enter your preferred **Sport** (running, basketball, calisthenics, cycling, football, hiking, etc.)
3. (Optional) Fill in available time, location, and extra notes
4. Click **🚀 Generate Touch Grass Challenge**
5. Go outside and complete it!

### Command Line

```bash
python cli.py \
  --level Advanced \
  --sport "calisthenics" \
  --time "35 minutes" \
  --location "grass field" \
  --notes "full body focus" \
  --model llama3.2
```

**Available arguments:**

| Argument | Default | Description |
|----------|---------|-------------|
| `--level` | Pemula | Pemula / Intermediate / Advanced |
| `--sport` | umum | Preferred sport |
| `--time` | - | Available time |
| `--location` | - | Preferred location |
| `--notes` | - | Additional notes |
| `--rule-based` | false | Force rule-based mode (no LLM) |
| `--model` | llama3.2 | Ollama model name |

---

## 🧠 How It Works / Cara Kerja

```
User Input
    ↓
┌─────────────────────────────┐
│     Challenge Engine        │
├─────────────────────────────┤
│  1. Is Ollama available?    │
│  2. Yes → Generate with     │
│         Local LLM + Prompt  │
│  3. No / Failed →           │
│         Rule-based Database │
└─────────────────────────────┘
    ↓
Outdoor Challenge + Touch Grass Moment
```

The **System Prompt** is strictly designed so the AI:
- Always generates **outdoor** activities
- Includes a "touch grass / soil / nature" moment
- Stays realistic and safe for the user's level
- Provides time estimate + intensity
- Gives supportive but firm motivation

---

## 📁 Project Structure / Struktur Project

```
touch-grass-sports-ai/
├── app.py                 # Web UI (Gradio)
├── cli.py                 # Command Line Interface
├── challenge_engine.py    # Main challenge generation logic
├── challenges_db.py       # Rule-based challenge database
├── prompts.py             # System prompt & templates
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

## 🤝 Contributing / Kontribusi

Contributions are very welcome! Some ideas:

- [ ] Daily progress & streak tracking
- [ ] More sports (outdoor swimming, climbing, trail running, etc.)
- [ ] Multi-language support
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

## 💡 Philosophy / Filosofi

Made for people who:

- Are tired of doomscrolling
- Want to move more in the real world
- Love sports but often feel lazy to go outside
- Believe that "touch grass" is the best medicine for an over-online brain

**Stop scrolling. Touch grass. Move your body.** 🏃‍♂️🌿

---

Made with 💚 for the outdoor movement.
