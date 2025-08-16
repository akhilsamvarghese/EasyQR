#!/usr/bin/env python3
"""
csv_qr.py
Interactive single-QR generator.
Batch mode: python3 csv_qr.py --batch my_links.csv
"""
import os
import sys
import qrcode
import pandas as pd
from PIL import Image
from typing import Optional

# ------------------------------------------------------------------
# Core helper: generate a single QR with optional logo
# ------------------------------------------------------------------
def make_qr(data: str, filename: str, logo_path: Optional[str] = None) -> None:
    """Create a QR code PNG, optionally overlay a logo."""
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    if logo_path and os.path.isfile(logo_path):
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo_size = int(img.size[0] * 0.25)
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
            img.paste(logo, pos, logo)
            print(f"✅ Logo added to {filename}")
        except Exception as e:
            print(f"⚠️ Could not add logo to {filename}: {e}")

    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    img.save(filename)
    print(f"✅ QR code saved: {filename}")

# ------------------------------------------------------------------
# Batch mode: ONLY when user gives a CSV via --batch <file>
# ------------------------------------------------------------------
def batch_mode(csv_file: str) -> None:
    if not os.path.isfile(csv_file):
        sys.exit(f"❌ CSV file not found: {csv_file}")

    df = pd.read_csv(csv_file)
    required = {"Platform", "URL", "Logos"}
    if not required.issubset(df.columns):
        missing = required - set(df.columns)
        sys.exit(f"❌ CSV missing columns: {missing}")

    for _, row in df.iterrows():
        platform = str(row["Platform"]).strip()
        url = str(row["URL"]).strip()
        logo = str(row["Logos"]).strip()
        filename = f"output/{platform}.png"
        make_qr(url, filename, logo if os.path.isfile(logo) else None)

# ------------------------------------------------------------------
# Interactive mode
# ------------------------------------------------------------------
def interactive_mode() -> None:
    data = input("Enter the link (or text) for the QR code: ").strip()
    filename = input("Enter the filename to save (without extension): ").strip()
    logo_path = input("Enter the logo file path (leave blank for no logo): ").strip()
    make_qr(data, f"{filename}.png", logo_path or None)

# ------------------------------------------------------------------
# CLI dispatcher
# ------------------------------------------------------------------
if __name__ == "__main__":
    if "--batch" in sys.argv:
        idx = sys.argv.index("--batch")
        if len(sys.argv) <= idx + 1:
            sys.exit("Usage: python3 csv_qr.py --batch <csv_file>")
        batch_mode(sys.argv[idx + 1])
    else:
        interactive_mode()