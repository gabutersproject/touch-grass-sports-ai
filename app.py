#!/usr/bin/env python3
"""
Touch Grass Sports AI - Offline Open Source Challenge Generator
Jalankan: python app.py
"""

import argparse
import gradio as gr
from challenge_engine import generate_challenge, OLLAMA_AVAILABLE


def create_challenge(level, sport, time_available, location, notes, use_ollama, model):
    if not level:
        level = "Pemula"
    if not sport:
        sport = "umum"
    
    result = generate_challenge(
        level=level,
        sport=sport,
        time_available=time_available,
        location=location,
        notes=notes,
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
            ### AI Offline yang memaksa kamu keluar rumah & berolahraga
            """,
            elem_classes=["main-title"]
        )
        gr.Markdown(
            "*100% lokal • Open Source • Tidak perlu internet setelah setup*",
            elem_classes=["subtitle"]
        )

        with gr.Row():
            with gr.Column(scale=1):
                level = gr.Radio(
                    choices=["Pemula", "Intermediate", "Advanced"],
                    value="Pemula",
                    label="Level Kebugaran"
                )
                sport = gr.Textbox(
                    label="Olahraga / Preferensi",
                    placeholder="Contoh: lari, basket, calisthenics, sepeda, sepakbola, hiking...",
                    value="lari"
                )
                time_available = gr.Textbox(
                    label="Waktu Tersedia",
                    placeholder="Contoh: 30 menit, 1 jam, pagi hari..."
                )
                location = gr.Textbox(
                    label="Lokasi / Preferensi",
                    placeholder="Contoh: taman dekat rumah, lapangan, trail..."
                )
                notes = gr.Textbox(
                    label="Catatan Tambahan",
                    placeholder="Contoh: cedera lutut, hujan ringan, ingin fokus kaki...",
                    lines=2
                )

                with gr.Accordion("Pengaturan AI (Opsional)", open=False):
                    use_ollama = gr.Checkbox(
                        label="Gunakan Ollama (Local LLM)",
                        value=default_ollama,
                        interactive=OLLAMA_AVAILABLE and not force_rule_based
                    )
                    model = gr.Textbox(
                        label="Nama Model Ollama",
                        value="llama3.2",
                        placeholder="llama3.2 / phi3 / gemma2:2b / qwen2.5:3b"
                    )
                    if not OLLAMA_AVAILABLE:
                        gr.Markdown("⚠️ Package `ollama` belum terinstall. Mode rule-based aktif.")
                    elif force_rule_based:
                        gr.Markdown("ℹ️ Mode rule-based dipaksa aktif (--rule-based).")

                btn = gr.Button("🚀 Generate Tantangan Touch Grass", variant="primary", size="lg")

            with gr.Column(scale=1):
                output = gr.Markdown(label="Tantangan Kamu")
                gr.Markdown("---")
                gr.Markdown(
                    """
                    **Tips:**
                    - Semakin spesifik inputmu, semakin bagus tantangannya
                    - Kalau pakai Ollama, pastikan model sudah di-pull (`ollama pull llama3.2`)
                    - Mode rule-based tetap bagus meski tanpa LLM
                    """
                )

        btn.click(
            fn=create_challenge,
            inputs=[level, sport, time_available, location, notes, use_ollama, model],
            outputs=output
        )

        # Contoh cepat
        gr.Examples(
            examples=[
                ["Pemula", "jalan kaki", "20 menit", "taman", "baru mulai olahraga"],
                ["Intermediate", "lari", "40 menit", "lapangan", ""],
                ["Advanced", "calisthenics", "35 menit", "rumput lapangan", "ingin full body"],
                ["Intermediate", "basket", "1 jam", "lapangan outdoor", "main sendiri"],
            ],
            inputs=[level, sport, time_available, location, notes],
            label="Contoh Cepat"
        )

    return demo


def main():
    parser = argparse.ArgumentParser(description="Touch Grass Sports AI")
    parser.add_argument(
        "--rule-based",
        action="store_true",
        help="Paksa mode rule-based (tanpa Ollama)"
    )
    parser.add_argument(
        "--share",
        action="store_true",
        help="Buat public Gradio link (butuh internet)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=7860,
        help="Port untuk server (default 7860)"
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
