import random
from typing import Optional
from prompts import SYSTEM_PROMPT, USER_TEMPLATE, RULE_BASED_FALLBACK
from challenges_db import get_matching_challenges

try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False


def generate_with_ollama(
    level: str,
    sport: str,
    time_available: str,
    location: str,
    notes: str,
    model: str = "llama3.2"
) -> str:
    """Generate challenge menggunakan Ollama lokal."""
    if not OLLAMA_AVAILABLE:
        raise RuntimeError("Ollama package tidak terinstall.")

    user_prompt = USER_TEMPLATE.format(
        level=level,
        sport=sport,
        time_available=time_available or "tidak ditentukan",
        location=location or "tidak ditentukan",
        notes=notes or "-"
    )

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            options={
                "temperature": 0.8,
                "top_p": 0.9,
            }
        )
        return response["message"]["content"]
    except Exception as e:
        return f"⚠️ Gagal memanggil Ollama: {str(e)}\n\nMenggunakan mode rule-based..."


def generate_rule_based(level: str, sport: str) -> str:
    """Generate dari database internal (100% offline, tanpa model)."""
    matches = get_matching_challenges(level, sport)
    challenge = random.choice(matches)

    return RULE_BASED_FALLBACK.format(
        title=challenge["title"],
        steps=challenge["steps"],
        duration=challenge["duration"],
        intensity=challenge["intensity"],
        touch_grass=challenge["touch_grass"],
        motivation=challenge["motivation"]
    )


def generate_challenge(
    level: str = "Pemula",
    sport: str = "umum",
    time_available: str = "",
    location: str = "",
    notes: str = "",
    use_ollama: bool = True,
    model: str = "llama3.2"
) -> str:
    """
    Main function untuk generate tantangan.
    Prioritas: Ollama jika tersedia & diminta, else rule-based.
    """
    if use_ollama and OLLAMA_AVAILABLE:
        try:
            # Cek apakah model tersedia
            models = ollama.list()
            available = [m["name"] for m in models.get("models", [])]
            if not any(model in m for m in available):
                # Coba model default lain
                for fallback in ["llama3.2", "phi3", "gemma2:2b", "qwen2.5:3b", "llama3.1"]:
                    if any(fallback in m for m in available):
                        model = fallback
                        break
                else:
                    return generate_rule_based(level, sport) + "\n\n_(Ollama terdeteksi tapi tidak ada model yang cocok. Pull model dulu: `ollama pull llama3.2`)_"

            result = generate_with_ollama(level, sport, time_available, location, notes, model)
            if result.startswith("⚠️"):
                return result + "\n\n" + generate_rule_based(level, sport)
            return result
        except Exception:
            return generate_rule_based(level, sport)
    
    return generate_rule_based(level, sport)
