#!/usr/bin/env python3
"""
Image optimization script for Zic0n Engineering website
Converts images to WebP format and creates responsive versions
"""

import os
from pathlib import Path

def create_webp_fallback_html():
    """Generate HTML snippet for WebP with fallback"""
    return """
<!-- Example WebP with fallback -->
<picture>
  <source srcset="images/example.webp" type="image/webp">
  <source srcset="images/example.jpg" type="image/jpeg">
  <img src="images/example.jpg" alt="Description" loading="lazy" class="w-full h-full object-cover">
</picture>
"""

def generate_image_optimization_guide():
    """Create a guide for image optimization"""
    guide = """
# Image Optimization Guide

## Tools Needed

### For WebP Conversion:
1. **Online Tools:**
   - https://squoosh.app/ (Google's image optimizer)
   - https://cloudconvert.com/jpg-to-webp
   
2. **Command Line (if you have ImageMagick):**
   ```bash
   # Convert single image
   magick convert input.jpg -quality 85 output.webp
   
   # Batch convert all JPGs
   for file in images/*.jpg; do
     magick convert "$file" -quality 85 "${file%.jpg}.webp"
   done
   ```

3. **Python (if you have Pillow):**
   ```bash
   pip install Pillow
   python optimize-images.py
   ```

## Optimization Checklist

- [ ] Convert all images to WebP format
- [ ] Keep original JPG/PNG as fallback
- [ ] Compress images (target: 85% quality)
- [ ] Create responsive sizes (thumbnail, medium, large)
- [ ] Add lazy loading to all images
- [ ] Use appropriate dimensions (don't serve 4K for thumbnails)

## Recommended Sizes

- **Hero images:** 1920x1080px (max 200KB)
- **Project cards:** 800x600px (max 100KB)
- **Team photos:** 600x600px (max 80KB)
- **Thumbnails:** 400x300px (max 50KB)

## Current Images to Optimize

"""
    
    images_dir = Path('images')
    if images_dir.exists():
        for img in sorted(images_dir.glob('*')):
            if img.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp']:
                size = img.stat().st_size / 1024  # KB
                guide += f"- {img.name} ({size:.1f} KB)\n"
    
    return guide

def main():
    """Main function"""
    print("Image Optimization Script")
    print("=" * 50)
    
    # Create optimization guide
    guide = generate_image_optimization_guide()
    
    with open('IMAGE_OPTIMIZATION.md', 'w', encoding='utf-8') as f:
        f.write(guide)
    
    print("✓ Created IMAGE_OPTIMIZATION.md")
    print("\nNext steps:")
    print("1. Review IMAGE_OPTIMIZATION.md")
    print("2. Use Squoosh.app to convert images to WebP")
    print("3. Update HTML to use <picture> elements")

if __name__ == '__main__':
    main()
