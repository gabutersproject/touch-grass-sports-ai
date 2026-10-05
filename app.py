#!/usr/bin/env python3
"""
Touch Grass Sports AI - Offline Open Source Challenge Generator
Run: python app.py
"""

import argparse
import gradio as gr
from challenge_engine import generate_challenge, OLLAMA_AVAILABLE


def create_challenge(level, sport, time_available, location, notes, lang, use_ollama, model):
    if not level:
        level = "Beginner"
    if not sport:
        sport = "general"

    result = generate_challenge(
        level=level,
        sport=sport,
        time_available=time_available,
        location=location,
        notes=notes,
        lang=lang,
        use_ollama=use_ollama,
        model=model
    )
    return result


def build_ui(force_rule_based: bool = False):
    default_ollama = OLLAMA_AVAILABLE and not force_rule_based

    with gr.Blocks(
        title="Touch Grass Sports AI",
        theme=gr.themes.Soft(primary_hue="green", secondary_hue="emerald"),
        css="""
        .main-title { text-align: center; margin-bottom: 0.5rem; }
        .subtitle { text-align: center; color: #555; margin-bottom: 1.5rem; }
        """
    ) as demo:
        gr.Markdown(
            """
            # 🌿 Touch Grass Sports AI
            ### Offline AI that forces you outside & get moving
            """,
            elem_classes=["main-title"]
        )
        gr.Markdown(
            "*100% local • Open Source • No internet needed after setup*",
            elem_classes=["subtitle"]
        )

        with gr.Row():
            with gr.Column(scale=1):
                lang = gr.Radio(
                    choices=[("English", "en"), ("Bahasa Indonesia", "id")],
                    value="en",
                    label="Language / Bahasa"
                )
                level = gr.Radio(
                    choices=["Beginner", "Intermediate", "Advanced"],
                    value="Beginner",
                    label="Fitness Level"
                )
                sport = gr.Textbox(
                    label="Sport / Preference",
                    placeholder="e.g. running, basketball, calisthenics, cycling, football, hiking...",
                    value="running"
                )
                time_available = gr.Textbox(
                    label="Available Time",
                    placeholder="e.g. 30 minutes, 1 hour, morning..."
                )
                location = gr.Textbox(
                    label="Location / Preference",
                    placeholder="e.g. nearby park, field, trail..."
                )
                notes = gr.Textbox(
                    label="Additional Notes",
                    placeholder="e.g. knee injury, light rain, want full body focus...",
                    lines=2
                )

                with gr.Accordion("AI Settings (Optional)", open=False):
                    use_ollama = gr.Checkbox(
                        label="Use Ollama (Local LLM)",
                        value=default_ollama,
                        interactive=OLLAMA_AVAILABLE and not force_rule_based
                    )
                    model = gr.Textbox(
                        label="Ollama Model Name",
                        value="llama3.2",
                        placeholder="llama3.2 / phi3 / gemma2:2b / qwen2.5:3b"
                    )
                    if not OLLAMA_AVAILABLE:
                        gr.Markdown("⚠️ `ollama` package is not installed. Rule-based mode is active.")
                    elif force_rule_based:
                        gr.Markdown("ℹ️ Rule-based mode is forced (--rule-based).")

                btn = gr.Button("🚀 Generate Touch Grass Challenge", variant="primary", size="lg")

            with gr.Column(scale=1):
                output = gr.Markdown(label="Your Challenge")
                gr.Markdown("---")
                gr.Markdown(
                    """
                    **Tips:**
                    - The more specific your input, the better the challenge
                    - If using Ollama, make sure the model is pulled (`ollama pull llama3.2`)
                    - Rule-based mode still works great without any LLM
                    """
                )

        btn.click(
            fn=create_challenge,
            inputs=[level, sport, time_available, location, notes, lang, use_ollama, model],
            outputs=output
        )

        gr.Examples(
            examples=[
                ["Beginner", "walking", "20 minutes", "park", "just starting to exercise", "en"],
                ["Intermediate", "running", "40 minutes", "field", "", "en"],
                ["Advanced", "calisthenics", "35 minutes", "grass field", "full body focus", "en"],
                ["Pemula", "jalan kaki", "20 menit", "taman", "baru mulai olahraga", "id"],
                ["Intermediate", "lari", "40 menit", "lapangan", "", "id"],
            ],
            inputs=[level, sport, time_available, location, notes, lang],
            label="Quick Examples"
        )

    return demo


def main():
    parser = argparse.ArgumentParser(description="Touch Grass Sports AI")
    parser.add_argument(
        "--rule-based",
        action="store_true",
        help="Force rule-based mode (no Ollama)"
    )
    parser.add_argument(
        "--share",
        action="store_true",
        help="Create a public Gradio link (requires internet)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=7860,
        help="Server port (default 7860)"
    )
    args = parser.parse_args()

    demo = build_ui(force_rule_based=args.rule_based)
    demo.launch(
        server_name="0.0.0.0",
        server_port=args.port,
        share=args.share,
        show_error=True
    )


if __name__ == "__main__":
    main()
