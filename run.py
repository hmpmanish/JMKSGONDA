#!/usr/bin/env python3
"""
Entry point for Jaymani Krishi Sewa
Run with: python run.py (or python app.py)
"""
import sys

# Ensure UTF-8 console output encoding on Windows terminals
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

from app import app

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("[*] JAYMANI KRISHI SEWA - Digital Agritech Marketplace & Bahi-Khata")
    print("    B.Tech Computer Science Capstone Evaluation-3 Working Prototype")
    print("    Running at: http://127.0.0.1:5000")
    print("=" * 70 + "\n")
    app.run(host="127.0.0.1", port=5000, debug=True)
