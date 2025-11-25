#!/usr/bin/env python3
"""
Script to replace the favicon from logo.png
Converts logo.png to favicon.ico and places it in static/img/

Usage:
    python utils/replace_favicon.py
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: PIL (Pillow) is required. Install it with: pip install Pillow")
    sys.exit(1)


def replace_favicon():
    """Convert logo.png to favicon.ico and place it in static/img/"""
    
    # Get the project root directory (parent of utils/)
    project_root = Path(__file__).parent.parent
    source_logo = project_root / 'logo.png'
    destination_dir = project_root / 'static' / 'img'
    favicon_path = destination_dir / 'favicon.ico'
    
    # Check if source logo exists
    if not source_logo.exists():
        print(f"Error: Source logo not found at {source_logo}")
        print("Please ensure logo.png exists in the project root directory.")
        sys.exit(1)
    
    # Ensure destination directory exists
    destination_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Open the source image
        img = Image.open(source_logo)
        
        # Convert to RGB if necessary (ICO doesn't support RGBA directly)
        if img.mode in ('RGBA', 'LA', 'P'):
            # Create a white background
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            if img.mode in ('RGBA', 'LA'):
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            else:
                img = img.convert('RGB')
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Resize to common favicon sizes (16x16, 32x32, 48x48)
        # ICO format can contain multiple sizes
        sizes = [(16, 16), (32, 32), (48, 48)]
        images = []
        
        for size in sizes:
            resized = img.resize(size, Image.Resampling.LANCZOS)
            images.append(resized)
        
        # Save as ICO with multiple sizes
        images[0].save(
            favicon_path,
            format='ICO',
            sizes=[(img.width, img.height) for img in images]
        )
        
        print(f"Favicon created successfully at {favicon_path}")
        print(f"  Source: {source_logo}")
        print(f"  Sizes: {', '.join([f'{w}x{h}' for w, h in sizes])}")
        
    except Exception as e:
        print(f"Error creating favicon: {e}")
        sys.exit(1)


if __name__ == '__main__':
    replace_favicon()

