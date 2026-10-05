# 🌿 Touch Grass Sports AI

**Open Source Offline AI** yang mendorongmu keluar rumah lewat tantangan olahraga nyata.

> "Stop scrolling. Touch grass. Move your body."

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Offline First](https://img.shields.io/badge/Offline-First-brightgreen.svg)](#)
[![Ollama Compatible](https://img.shields.io/badge/Ollama-Compatible-orange.svg)](https://ollama.com)

Aplikasi AI lokal **100% offline** yang menghasilkan tantangan olahraga outdoor personal.  
Tidak butuh internet setelah setup. Privasi penuh. Open source.

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
|-------|---------|
| **100% Offline** | Berjalan lokal pakai Ollama atau mode rule-based tanpa model sama sekali |
| **Tema Touch Grass** | Setiap tantangan wajib dilakukan di luar rumah + elemen menyentuh rumput/tanah/alam |
| **Personalisasi** | Level kebugaran, jenis olahraga, waktu tersedia, lokasi, dan catatan khusus |
| **Dua Interface** | Web UI modern (Gradio) + CLI ringan |
| **Dua Engine** | Local LLM (Ollama) untuk tantangan kreatif, atau database rule-based yang cepat |
| **Privasi Total** | Tidak ada data yang dikirim ke cloud |
| **Open Source** | MIT License — bebas dipakai, dimodifikasi, dan dibagikan |

---

## 🎯 Contoh Tantangan

**Pemula – Lari**
> Lari santai 1–1.5 km di taman → 15x jumping jack di rumput → sentuh rumput dengan kedua tangan.

**Intermediate – Basket**
> Main 20–30 menit di lapangan outdoor → setiap miss shoot lakukan 5 push-up di rumput → cool down duduk di rumput.

**Advanced – Calisthenics**
> 5 putaran HIIT di lapangan rumput (burpee, jump squat, sprint, explosive push-up) → finisher mountain climber + plank.

---

## 🛠️ Persyaratan Sistem

- **Python** 3.9 atau lebih tinggi
- **Ollama** (opsional, direkomendasikan untuk pengalaman terbaik)
- Model lokal kecil (contoh):
  - `llama3.2` (direkomendasikan)
  - `phi3`
  - `gemma2:2b`
  - `qwen2.5:3b`
- RAM minimal: 4 GB (rule-based) / 8 GB+ (dengan model)

---

## 🚀 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/gabutersproject/touch-grass-sports-ai.git
cd touch-grass-sports-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. (Opsional) Install & Setup Ollama

1. Download Ollama dari [https://ollama.com](https://ollama.com)
2. Pull model kecil:

```bash
ollama pull llama3.2
# atau
ollama pull phi3
ollama pull gemma2:2b
```

### 4. Jalankan Aplikasi

**Web UI (disarankan):**
```bash
python app.py
```
Buka browser → `http://localhost:7860`

**Mode Rule-based saja (tanpa Ollama):**
```bash
python app.py --rule-based
```

**CLI:**
```bash
python cli.py --level Intermediate --sport "lari" --time "40 menit"
```

---

## 📖 Cara Penggunaan

### Web Interface

1. Pilih **Level Kebugaran** (Pemula / Intermediate / Advanced)
2. Isi **Olahraga / Preferensi** (contoh: lari, basket, calisthenics, sepeda, sepakbola, hiking)
3. (Opsional) Isi waktu tersedia, lokasi, dan catatan tambahan
4. Klik **🚀 Generate Tantangan Touch Grass**
5. Kerjakan tantangan tersebut di luar rumah!

### Command Line

```bash
python cli.py \
  --level Advanced \
  --sport "calisthenics" \
  --time "35 menit" \
  --location "lapangan rumput" \
  --notes "fokus full body" \
  --model llama3.2
```

**Argumen yang tersedia:**

| Argumen | Default | Keterangan |
|---------|---------|----------|
| `--level` | Pemula | Pemula / Intermediate / Advanced |
| `--sport` | umum | Jenis olahraga |
| `--time` | - | Waktu yang tersedia |
| `--location` | - | Preferensi lokasi |
| `--notes` | - | Catatan tambahan |
| `--rule-based` | false | Paksa mode tanpa LLM |
| `--model` | llama3.2 | Nama model Ollama |

---

## 🧠 Cara Kerja

```
User Input
    ↓
Challenge Engine
  1. Cek Ollama tersedia?
  2. Ya → Generate dengan Local LLM + Prompt
  3. Tidak / Gagal → Rule-based Database
    ↓
Tantangan Outdoor + Touch Grass Moment
```

**System Prompt** dirancang ketat agar AI:
- Selalu menghasilkan aktivitas **outdoor**
- Menyertakan momen "sentuh rumput / tanah / alam"
- Realistis dan aman sesuai level
- Memberikan estimasi waktu + intensitas
- Memberikan motivasi yang supportive tapi tegas

---

## 📁 Struktur Project

```
touch-grass-sports-ai/
├── app.py                 # Web UI (Gradio)
├── cli.py                 # Command Line Interface
├── challenge_engine.py    # Logic utama generate tantangan
├── challenges_db.py       # Database tantangan rule-based
├── prompts.py             # System prompt & template
├── requirements.txt       # Dependensi Python
├── LICENSE                # MIT License
└── README.md              # Dokumentasi ini
```

---

## 🧩 Dependensi

```txt
gradio>=4.0.0
ollama>=0.3.0
pydantic>=2.0.0
```

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Beberapa ide yang bisa dikerjakan:

- [ ] Tracking progress & streak harian
- [ ] Lebih banyak olahraga (renang outdoor, climbing, trail running, dll)
- [ ] Multi-bahasa (English, dll)
- [ ] Voice input / Text-to-Speech
- [ ] Export tantangan ke Markdown / PDF / Calendar
- [ ] Mode "Daily Challenge" otomatis
- [ ] Integrasi dengan sensor HP (langkah, GPS) di masa depan

**Cara kontribusi:**
1. Fork repository ini
2. Buat branch baru (`git checkout -b fitur-keren`)
3. Commit perubahanmu
4. Push dan buat Pull Request

---

## 📜 License

Proyek ini dilisensikan di bawah **MIT License**.  
Lihat file [LICENSE](LICENSE) untuk detail lengkap.

---

## 💡 Filosofi

Dibuat untuk orang-orang yang:

- Capek doomscrolling
- Ingin lebih banyak bergerak di dunia nyata
- Suka olahraga tapi sering males keluar rumah
- Percaya bahwa "touch grass" adalah obat terbaik untuk otak yang terlalu online

**Stop scrolling. Touch grass. Move your body.** 🏃‍♂️🌿

---

Made with 💚 for the outdoor movement.
