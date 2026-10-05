#!/usr/bin/env python3
"""
CLI version of Touch Grass Sports AI
Jalankan: python cli.py
"""

import argparse
from challenge_engine import generate_challenge


def main():
    parser = argparse.ArgumentParser(
        description="🌿 Touch Grass Sports AI - Generate tantangan olahraga outdoor"
    )
    parser.add_argument("--level", default="Pemula", choices=["Pemula", "Intermediate", "Advanced"])
    parser.add_argument("--sport", default="umum", help="Olahraga favorit")
    parser.add_argument("--time", default="", help="Waktu tersedia")
    parser.add_argument("--location", default="", help="Lokasi preferensi")
    parser.add_argument("--notes", default="", help="Catatan tambahan")
    parser.add_argument("--rule-based", action="store_true", help="Paksa mode tanpa Ollama")
    parser.add_argument("--model", default="llama3.2", help="Model Ollama")

    args = parser.parse_args()

    print("\n🌿 Generating tantangan Touch Grass...\n")
    result = generate_challenge(
        level=args.level,
        sport=args.sport,
        time_available=args.time,
        location=args.location,
        notes=args.notes,
        use_ollama=not args.rule_based,
        model=args.model
    )
    print(result)
    print("\n---")
    print("Sekarang keluar rumah dan kerjakan! 🏃‍♂️")


if __name__ == "__main__":
    main()
