"""
Database tantangan rule-based untuk mode offline tanpa LLM.
"""

CHALLENGES = {
    "pemula": [
        {
            "title": "Jalan Santai + Sentuh Rumput",
            "sport": ["jalan kaki", "hiking", "umum"],
            "steps": "1. Keluar rumah dan jalan kaki minimal 15-20 menit di area terbuka.\n2. Cari rumput atau tanah.\n3. Lepas sepatu sebentar dan rasakan rumput di telapak kaki (atau sentuh dengan tangan).\n4. Lakukan 10x deep breath sambil berdiri di rumput.",
            "duration": "20-25 menit",
            "intensity": "Rendah",
            "touch_grass": "Rasakan rumput di kaki selama minimal 30 detik.",
            "motivation": "Langkah kecil hari ini lebih baik daripada tidak sama sekali. Keluar sekarang!"
        },
        {
            "title": "Lari Ringan Taman",
            "sport": ["lari", "umum"],
            "steps": "1. Pergi ke taman atau lapangan terdekat.\n2. Lari santai 1-1.5 km (boleh jalan-lari).\n3. Di akhir, lakukan 15x jumping jack di atas rumput.\n4. Sentuh rumput dengan kedua tangan dan ucapkan terima kasih ke alam.",
            "duration": "15-25 menit",
            "intensity": "Rendah-Sedang",
            "touch_grass": "Sentuh rumput setelah selesai lari.",
            "motivation": "Tubuhmu butuh udara segar. Gerak sekarang!"
        },
        {
            "title": "Circuit Rumput Pemula",
            "sport": ["calisthenics", "umum", "bodyweight"],
            "steps": "1. Cari area rumput atau lapangan.\n2. Lakukan 3 set: 8 push-up (bisa knee), 10 squat, 15 detik plank.\n3. Istirahat 1 menit antar set sambil berdiri di rumput.\n4. Di akhir, berbaring telentang di rumput selama 1 menit.",
            "duration": "15-20 menit",
            "intensity": "Rendah-Sedang",
            "touch_grass": "Berbaring di rumput di akhir sesi.",
            "motivation": "Tidak perlu gym. Rumput adalah gym terbaikmu hari ini."
        }
    ],
    "intermediate": [
        {
            "title": "Tempo Run + Grass Touch",
            "sport": ["lari"],
            "steps": "1. Lari 3-4 km di luar rumah dengan tempo sedang.\n2. Setiap 1 km, berhenti sebentar dan sentuh rumput/tanah.\n3. Di akhir, lakukan 3x20 detik high knees di atas rumput.\n4. Stretch sambil duduk di rumput.",
            "duration": "30-40 menit",
            "intensity": "Sedang",
            "touch_grass": "Sentuh rumput setiap kilometer.",
            "motivation": "Kamu lebih kuat dari alasanmu untuk tidak keluar. Gas!"
        },
        {
            "title": "Basket Outdoor Session",
            "sport": ["basket", "bola basket"],
            "steps": "1. Pergi ke lapangan basket terbuka.\n2. Mainkan 20-30 menit (dribble, shooting, atau 1v1 jika ada lawan).\n3. Setiap kali gagal shoot, lakukan 5 push-up di rumput sekitar lapangan.\n4. Di akhir, duduk di rumput dan refleksi permainanmu.",
            "duration": "30-40 menit",
            "intensity": "Sedang-Tinggi",
            "touch_grass": "Push-up di rumput setiap miss.",
            "motivation": "Lapangan menunggu. Bola tidak akan bergerak sendiri."
        },
        {
            "title": "Sepeda + Explore",
            "sport": ["sepeda", "bersepeda"],
            "steps": "1. Sepeda minimal 8-12 km di rute outdoor.\n2. Berhenti di 2-3 titik hijau, turun, dan sentuh rumput/pohon.\n3. Di salah satu titik, lakukan 20 squats.\n4. Foto salah satu momen 'touch grass'-mu.",
            "duration": "40-60 menit",
            "intensity": "Sedang",
            "touch_grass": "Minimal 2x turun dan sentuh alam.",
            "motivation": "Roda berputar, pikiran jernih. Ayo berangkat!"
        },
        {
            "title": "Full Body Outdoor Circuit",
            "sport": ["calisthenics", "umum"],
            "steps": "1. Cari lapangan rumput.\n2. Circuit 4 putaran: 12 push-up, 15 squat jump, 10 burpee, 20 mountain climber.\n3. Istirahat 60-90 detik antar putaran sambil berjalan di rumput.\n4. Finisher: 1 menit wall sit atau plank di rumput.",
            "duration": "25-35 menit",
            "intensity": "Sedang-Tinggi",
            "touch_grass": "Semua gerakan dilakukan di atas rumput.",
            "motivation": "Tidak ada mesin gym yang bisa mengalahkan lapangan terbuka."
        }
    ],
    "advanced": [
        {
            "title": "Long Run + Nature Connection",
            "sport": ["lari"],
            "steps": "1. Lari 7-10 km di rute outdoor (taman, trail, atau jalanan hijau).\n2. Setiap 2 km, berhenti 30 detik, sentuh rumput/tanah, dan lakukan 10 deep squat.\n3. Di 2 km terakhir, tingkatkan pace.\n4. Setelah selesai, barefoot walk 5 menit di rumput jika memungkinkan.",
            "duration": "50-75 menit",
            "intensity": "Tinggi",
            "touch_grass": "Barefoot walk di akhir + touch di setiap checkpoint.",
            "motivation": "Ini levelmu. Buktikan kamu pantas disebut atlet outdoor."
        },
        {
            "title": "HIIT Grass Destroyer",
            "sport": ["calisthenics", "hiit", "umum"],
            "steps": "1. Cari area rumput luas.\n2. 5 putaran: 15 burpee, 20 jump squat, 30 detik sprint di tempat, 15 push-up explosive.\n3. Istirahat aktif 45 detik (jalan di rumput).\n4. Finisher: 2 menit max effort mountain climber + 1 menit plank.",
            "duration": "30-40 menit",
            "intensity": "Sangat Tinggi",
            "touch_grass": "Semua di rumput. Rasakan tanah di setiap gerakan.",
            "motivation": "Sakit di lapangan lebih berharga daripada nyaman di kamar."
        },
        {
            "title": "Sepakbola / Futsal Outdoor Grind",
            "sport": ["sepakbola", "futsal", "bola"],
            "steps": "1. Main minimal 40-60 menit di lapangan terbuka.\n2. Fokus pada intensitas tinggi (interval sprint + technical drill).\n3. Setiap istirahat, lakukan 10 push-up di rumput.\n4. Setelah main, cool down sambil duduk/berbaring di rumput 5 menit.",
            "duration": "50-70 menit",
            "intensity": "Tinggi",
            "touch_grass": "Push-up di rumput + cool down di rumput.",
            "motivation": "Lapangan adalah rumah kedua. Main seolah tidak ada hari esok."
        }
    ]
}

def get_matching_challenges(level: str, sport: str) -> list:
    level = level.lower().strip()
    sport = sport.lower().strip()
    
    if level not in CHALLENGES:
        level = "pemula"
    
    matches = []
    for ch in CHALLENGES[level]:
        if any(s in sport for s in ch["sport"]) or "umum" in ch["sport"]:
            matches.append(ch)
    
    # Jika tidak ada match spesifik, ambil semua di level itu
    if not matches:
        matches = CHALLENGES[level]
    
    return matches
