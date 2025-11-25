# Utils Directory

Utility scripts for maintaining the Arcane Forge documentation site.

## replace_favicon.py

Converts `logo.png` to `favicon.ico` and places it in `static/img/`.

### Requirements

- Python 3.6+
- Pillow library: `pip install Pillow`

### Usage

```bash
python utils/replace_favicon.py
```

### What it does

1. Reads `logo.png` from the project root
2. Converts it to RGB format (if needed)
3. Creates multiple sizes (16x16, 32x32, 48x48)
4. Saves as `static/img/favicon.ico` with all sizes embedded

### Notes

- The script automatically handles transparency by placing the logo on a white background
- If `logo.png` is updated, run this script again to update the favicon

