
## **EasyQR** – a tiny, self-contained Python utility that

1. **Interactively** creates one QR code at a time, *or*  
2. **In batch** creates one QR code **per row** in any CSV file you supply.

---

## 🚀 Quick start

```bash
# 1. Install deps
pip install qrcode pillow pandas

# 2. Clone or copy the two files
qrcode_generator.py
my_links.csv   # optional – any CSV you like

# 3. Run
python3 easyqr.py                    # interactive mode
python3 easyqr.py --batch links.csv  # batch mode
```

---

## 🗂️ CSV format for batch mode

Create any CSV with **exactly** these headers:

| Platform | URL                            | Logos               |
|----------|--------------------------------|---------------------|
| LinkedIn | https://linkedin.com/company   | Logos/linkedin.png  |
| Website  | https://example.com            | Logos/website.png   |
| X        | https://x.com/acme             | Logos/x.png         |

- **Relative paths** in `Logos` are resolved from the folder where you run the script.  
- Blank or missing logo files → QR code without logo.

---

## 📁 Output

- **Interactive mode**: `<filename>.png` in the current directory.  
- **Batch mode**: `output/<Platform>.png` (folder auto-created).

---

## 🧪 Interactive example

```text
$ python3 easyqr.py.py
Enter the link (or text) for the QR code: https://youtu.be/abc123
Enter the filename to save (without extension): yt_demo
Enter the logo file path (leave blank for no logo): Logos/youtube.png
✅ Logo added to yt_demo.png
✅ QR code saved: yt_demo.png
```

---

## 🧩 Batch example

```text
$ python3 easyqr.py --batch my_links.csv
✅ Logo added to output/LinkedIn.png
✅ QR code saved: output/Website.png
✅ QR code saved: output/X.png
```

---

## 📄 Requirements

- `qrcode`
- `pillow`  
- `pandas`

---
