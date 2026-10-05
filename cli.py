#!/usr/bin/env python3
"""
CLI version of Touch Grass Sports AI
Run: python cli.py
"""

import argparse
from challenge_engine import generate_challenge


def main():
    parser = argparse.ArgumentParser(
        description="🌿 Touch Grass Sports AI - Generate outdoor sports challenges"
    )
    parser.add_argument("--level", default="Beginner",
                        choices=["Beginner", "Intermediate", "Advanced", "Pemula"],
                        help="Fitness level")
    parser.add_argument("--sport", default="general", help="Preferred sport")
    parser.add_argument("--time", default="", help="Available time")
    parser.add_argument("--location", default="", help="Preferred location")
    parser.add_argument("--notes", default="", help="Additional notes")
    parser.add_argument("--lang", default="en", choices=["en", "id"],
                        help="Language: en (English) or id (Indonesian)")
    parser.add_argument("--rule-based", action="store_true",
                        help="Force rule-based mode (no Ollama)")
    parser.add_argument("--model", default="llama3.2", help="Ollama model name")

    args = parser.parse_args()

    print("\n🌿 Generating Touch Grass challenge...\n" if args.lang == "en"
          else "\n🌿 Generating tantangan Touch Grass...\n")

    result = generate_challenge(
        level=args.level,
        sport=args.sport,
        time_available=args.time,
        location=args.location,
        notes=args.notes,
        lang=args.lang,
        use_ollama=not args.rule_based,
        model=args.model
    )
    print(result)
    print("\n---")
    print("Now go outside and do it! 🏃‍♂️" if args.lang == "en"
          else "Sekarang keluar rumah dan kerjakan! 🏃‍♂️")


if __name__ == "__main__":
    main()
