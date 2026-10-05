"""
Rule-based challenge database for offline mode (no LLM).
Supports multiple languages.
"""

CHALLENGES = {
    "en": {
        "beginner": [
            {
                "title": "Easy Walk + Touch Grass",
                "sport": ["walking", "hiking", "general"],
                "steps": "1. Go outside and walk for at least 15-20 minutes in an open area.\n2. Find some grass or soil.\n3. Take off your shoes briefly and feel the grass under your feet (or touch it with your hands).\n4. Take 10 deep breaths while standing on the grass.",
                "duration": "20-25 minutes",
                "intensity": "Low",
                "touch_grass": "Feel the grass under your feet for at least 30 seconds.",
                "motivation": "A small step today is better than nothing at all. Get outside now!"
            },
            {
                "title": "Light Park Run",
                "sport": ["running", "general"],
                "steps": "1. Go to a nearby park or field.\n2. Jog easily for 1-1.5 km (walk-run is fine).\n3. At the end, do 15 jumping jacks on the grass.\n4. Touch the grass with both hands and say thank you to nature.",
                "duration": "15-25 minutes",
                "intensity": "Low-Medium",
                "touch_grass": "Touch the grass after finishing your run.",
                "motivation": "Your body needs fresh air. Move now!"
            },
            {
                "title": "Beginner Grass Circuit",
                "sport": ["calisthenics", "general", "bodyweight"],
                "steps": "1. Find a grassy area or field.\n2. Do 3 sets: 8 push-ups (knee push-ups ok), 10 squats, 15-second plank.\n3. Rest 1 minute between sets while standing on the grass.\n4. At the end, lie on your back on the grass for 1 minute.",
                "duration": "15-20 minutes",
                "intensity": "Low-Medium",
                "touch_grass": "Lie on the grass at the end of the session.",
                "motivation": "No gym needed. The grass is your best gym today."
            }
        ],
        "intermediate": [
            {
                "title": "Tempo Run + Grass Touch",
                "sport": ["running"],
                "steps": "1. Run 3-4 km outdoors at a moderate tempo.\n2. Every 1 km, stop briefly and touch the grass/soil.\n3. At the end, do 3x20 seconds of high knees on the grass.\n4. Stretch while sitting on the grass.",
                "duration": "30-40 minutes",
                "intensity": "Medium",
                "touch_grass": "Touch the grass every kilometer.",
                "motivation": "You are stronger than your excuses. Go!"
            },
            {
                "title": "Outdoor Basketball Session",
                "sport": ["basketball"],
                "steps": "1. Go to an outdoor basketball court.\n2. Play for 20-30 minutes (dribble, shooting, or 1v1 if you have a partner).\n3. Every time you miss a shot, do 5 push-ups on the surrounding grass.\n4. At the end, sit on the grass and reflect on your game.",
                "duration": "30-40 minutes",
                "intensity": "Medium-High",
                "touch_grass": "Push-ups on the grass for every miss.",
                "motivation": "The court is waiting. The ball won't move by itself."
            },
            {
                "title": "Cycling + Explore",
                "sport": ["cycling", "bike"],
                "steps": "1. Cycle at least 8-12 km on an outdoor route.\n2. Stop at 2-3 green spots, get off, and touch the grass/trees.\n3. At one of the spots, do 20 squats.\n4. Take a photo of one of your 'touch grass' moments.",
                "duration": "40-60 minutes",
                "intensity": "Medium",
                "touch_grass": "Get off and touch nature at least twice.",
                "motivation": "Wheels turn, mind clears. Let's go!"
            },
            {
                "title": "Full Body Outdoor Circuit",
                "sport": ["calisthenics", "general"],
                "steps": "1. Find a grass field.\n2. 4 rounds: 12 push-ups, 15 squat jumps, 10 burpees, 20 mountain climbers.\n3. Rest 60-90 seconds between rounds while walking on the grass.\n4. Finisher: 1-minute wall sit or plank on the grass.",
                "duration": "25-35 minutes",
                "intensity": "Medium-High",
                "touch_grass": "All movements performed on the grass.",
                "motivation": "No gym machine can beat an open field."
            }
        ],
        "advanced": [
            {
                "title": "Long Run + Nature Connection",
                "sport": ["running"],
                "steps": "1. Run 7-10 km on an outdoor route (park, trail, or green roads).\n2. Every 2 km, stop for 30 seconds, touch the grass/soil, and do 10 deep squats.\n3. In the last 2 km, increase the pace.\n4. After finishing, barefoot walk for 5 minutes on the grass if possible.",
                "duration": "50-75 minutes",
                "intensity": "High",
                "touch_grass": "Barefoot walk at the end + touch at every checkpoint.",
                "motivation": "This is your level. Prove you deserve to be called an outdoor athlete."
            },
            {
                "title": "HIIT Grass Destroyer",
                "sport": ["calisthenics", "hiit", "general"],
                "steps": "1. Find a wide grassy area.\n2. 5 rounds: 15 burpees, 20 jump squats, 30-second sprint in place, 15 explosive push-ups.\n3. Active rest 45 seconds (walk on the grass).\n4. Finisher: 2 minutes max effort mountain climbers + 1-minute plank.",
                "duration": "30-40 minutes",
                "intensity": "Very High",
                "touch_grass": "Everything on the grass. Feel the ground with every movement.",
                "motivation": "Pain on the field is more valuable than comfort in your room."
            },
            {
                "title": "Football / Soccer Outdoor Grind",
                "sport": ["football", "soccer", "futsal"],
                "steps": "1. Play for at least 40-60 minutes on an outdoor field.\n2. Focus on high intensity (sprint intervals + technical drills).\n3. During every break, do 10 push-ups on the grass.\n4. After playing, cool down by sitting/lying on the grass for 5 minutes.",
                "duration": "50-70 minutes",
                "intensity": "High",
                "touch_grass": "Push-ups on the grass + cool down on the grass.",
                "motivation": "The field is your second home. Play like there's no tomorrow."
            }
        ]
    },
    "id": {
        "beginner": [
            {
                "title": "Jalan Santai + Sentuh Rumput",
                "sport": ["jalan kaki", "hiking", "umum", "walking", "general"],
                "steps": "1. Keluar rumah dan jalan kaki minimal 15-20 menit di area terbuka.\n2. Cari rumput atau tanah.\n3. Lepas sepatu sebentar dan rasakan rumput di telapak kaki (atau sentuh dengan tangan).\n4. Lakukan 10x deep breath sambil berdiri di rumput.",
                "duration": "20-25 menit",
                "intensity": "Rendah",
                "touch_grass": "Rasakan rumput di kaki selama minimal 30 detik.",
                "motivation": "Langkah kecil hari ini lebih baik daripada tidak sama sekali. Keluar sekarang!"
            },
            {
                "title": "Lari Ringan Taman",
                "sport": ["lari", "running", "umum", "general"],
                "steps": "1. Pergi ke taman atau lapangan terdekat.\n2. Lari santai 1-1.5 km (boleh jalan-lari).\n3. Di akhir, lakukan 15x jumping jack di atas rumput.\n4. Sentuh rumput dengan kedua tangan dan ucapkan terima kasih ke alam.",
                "duration": "15-25 menit",
                "intensity": "Rendah-Sedang",
                "touch_grass": "Sentuh rumput setelah selesai lari.",
                "motivation": "Tubuhmu butuh udara segar. Gerak sekarang!"
            },
            {
                "title": "Circuit Rumput Pemula",
                "sport": ["calisthenics", "umum", "bodyweight", "general"],
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
                "sport": ["lari", "running"],
                "steps": "1. Lari 3-4 km di luar rumah dengan tempo sedang.\n2. Setiap 1 km, berhenti sebentar dan sentuh rumput/tanah.\n3. Di akhir, lakukan 3x20 detik high knees di atas rumput.\n4. Stretch sambil duduk di rumput.",
                "duration": "30-40 menit",
                "intensity": "Sedang",
                "touch_grass": "Sentuh rumput setiap kilometer.",
                "motivation": "Kamu lebih kuat dari alasanmu untuk tidak keluar. Gas!"
            },
            {
                "title": "Basket Outdoor Session",
                "sport": ["basket", "basketball", "bola basket"],
                "steps": "1. Pergi ke lapangan basket terbuka.\n2. Mainkan 20-30 menit (dribble, shooting, atau 1v1 jika ada lawan).\n3. Setiap kali gagal shoot, lakukan 5 push-up di rumput sekitar lapangan.\n4. Di akhir, duduk di rumput dan refleksi permainanmu.",
                "duration": "30-40 menit",
                "intensity": "Sedang-Tinggi",
                "touch_grass": "Push-up di rumput setiap miss.",
                "motivation": "Lapangan menunggu. Bola tidak akan bergerak sendiri."
            },
            {
                "title": "Sepeda + Explore",
                "sport": ["sepeda", "bersepeda", "cycling", "bike"],
                "steps": "1. Sepeda minimal 8-12 km di rute outdoor.\n2. Berhenti di 2-3 titik hijau, turun, dan sentuh rumput/pohon.\n3. Di salah satu titik, lakukan 20 squats.\n4. Foto salah satu momen 'touch grass'-mu.",
                "duration": "40-60 menit",
                "intensity": "Sedang",
                "touch_grass": "Minimal 2x turun dan sentuh alam.",
                "motivation": "Roda berputar, pikiran jernih. Ayo berangkat!"
            },
            {
                "title": "Full Body Outdoor Circuit",
                "sport": ["calisthenics", "umum", "general"],
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
                "sport": ["lari", "running"],
                "steps": "1. Lari 7-10 km di rute outdoor (taman, trail, atau jalanan hijau).\n2. Setiap 2 km, berhenti 30 detik, sentuh rumput/tanah, dan lakukan 10 deep squat.\n3. Di 2 km terakhir, tingkatkan pace.\n4. Setelah selesai, barefoot walk 5 menit di rumput jika memungkinkan.",
                "duration": "50-75 menit",
                "intensity": "Tinggi",
                "touch_grass": "Barefoot walk di akhir + touch di setiap checkpoint.",
                "motivation": "Ini levelmu. Buktikan kamu pantas disebut atlet outdoor."
            },
            {
                "title": "HIIT Grass Destroyer",
                "sport": ["calisthenics", "hiit", "umum", "general"],
                "steps": "1. Cari area rumput luas.\n2. 5 putaran: 15 burpee, 20 jump squat, 30 detik sprint di tempat, 15 push-up explosive.\n3. Istirahat aktif 45 detik (jalan di rumput).\n4. Finisher: 2 menit max effort mountain climber + 1 menit plank.",
                "duration": "30-40 menit",
                "intensity": "Sangat Tinggi",
                "touch_grass": "Semua di rumput. Rasakan tanah di setiap gerakan.",
                "motivation": "Sakit di lapangan lebih berharga daripada nyaman di kamar."
            },
            {
                "title": "Sepakbola / Futsal Outdoor Grind",
                "sport": ["sepakbola", "futsal", "bola", "football", "soccer"],
                "steps": "1. Main minimal 40-60 menit di lapangan terbuka.\n2. Fokus pada intensitas tinggi (interval sprint + technical drill).\n3. Setiap istirahat, lakukan 10 push-up di rumput.\n4. Setelah main, cool down sambil duduk/berbaring di rumput 5 menit.",
                "duration": "50-70 menit",
                "intensity": "Tinggi",
                "touch_grass": "Push-up di rumput + cool down di rumput.",
                "motivation": "Lapangan adalah rumah kedua. Main seolah tidak ada hari esok."
            }
        ]
    }
}

LEVEL_MAP = {
    "pemula": "beginner",
    "beginner": "beginner",
    "intermediate": "intermediate",
    "advanced": "advanced",
    "mahir": "advanced"
}

def get_matching_challenges(level: str, sport: str, lang: str = "en") -> list:
    lang = lang.lower().strip()
    if lang not in CHALLENGES:
        lang = "en"

    level_key = LEVEL_MAP.get(level.lower().strip(), "beginner")
    sport = sport.lower().strip()

    lang_challenges = CHALLENGES[lang]
    if level_key not in lang_challenges:
        level_key = "beginner"

    matches = []
    for ch in lang_challenges[level_key]:
        if any(s in sport for s in ch["sport"]) or "general" in ch["sport"] or "umum" in ch["sport"]:
            matches.append(ch)

    if not matches:
        matches = lang_challenges[level_key]

    return matches
