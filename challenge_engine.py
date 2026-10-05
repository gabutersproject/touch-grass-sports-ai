import random
from prompts import get_system_prompt, get_user_template, get_fallback_template
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
    lang: str = "en",
    model: str = "llama3.2"
) -> str:
    """Generate challenge using local Ollama."""
    if not OLLAMA_AVAILABLE:
        raise RuntimeError("Ollama package is not installed.")

    user_prompt = get_user_template(lang).format(
        level=level,
        sport=sport,
        time_available=time_available or ("not specified" if lang == "en" else "tidak ditentukan"),
        location=location or ("not specified" if lang == "en" else "tidak ditentukan"),
        notes=notes or "-"
    )

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": get_system_prompt(lang)},
                {"role": "user", "content": user_prompt}
            ],
            options={
                "temperature": 0.8,
                "top_p": 0.9,
            }
        )
        return response["message"]["content"]
    except Exception as e:
        msg = f"⚠️ Failed to call Ollama: {str(e)}\n\nFalling back to rule-based mode..." if lang == "en" else f"⚠️ Gagal memanggil Ollama: {str(e)}\n\nMenggunakan mode rule-based..."
        return msg


def generate_rule_based(level: str, sport: str, lang: str = "en") -> str:
    """Generate from internal database (100% offline, no model)."""
    matches = get_matching_challenges(level, sport, lang)
    challenge = random.choice(matches)

    return get_fallback_template(lang).format(
        title=challenge["title"],
        steps=challenge["steps"],
        duration=challenge["duration"],
        intensity=challenge["intensity"],
        touch_grass=challenge["touch_grass"],
        motivation=challenge["motivation"]
    )


def generate_challenge(
    level: str = "Beginner",
    sport: str = "general",
    time_available: str = "",
    location: str = "",
    notes: str = "",
    lang: str = "en",
    use_ollama: bool = True,
    model: str = "llama3.2"
) -> str:
    """
    Main function to generate a challenge.
    Priority: Ollama if available & requested, else rule-based.
    """
    lang = lang.lower().strip()
    if lang not in ("en", "id"):
        lang = "en"

    if use_ollama and OLLAMA_AVAILABLE:
        try:
            models = ollama.list()
            available = [m["name"] for m in models.get("models", [])]
            if not any(model in m for m in available):
                for fallback in ["llama3.2", "phi3", "gemma2:2b", "qwen2.5:3b", "llama3.1"]:
                    if any(fallback in m for m in available):
                        model = fallback
                        break
                else:
                    tip = "_(Ollama detected but no suitable model found. Pull a model first: `ollama pull llama3.2`)_" if lang == "en" else "_(Ollama terdeteksi tapi tidak ada model yang cocok. Pull model dulu: `ollama pull llama3.2`)_"
                    return generate_rule_based(level, sport, lang) + "\n\n" + tip

            result = generate_with_ollama(level, sport, time_available, location, notes, lang, model)
            if result.startswith("⚠️"):
                return result + "\n\n" + generate_rule_based(level, sport, lang)
            return result
        except Exception:
            return generate_rule_based(level, sport, lang)

    return generate_rule_based(level, sport, lang)
