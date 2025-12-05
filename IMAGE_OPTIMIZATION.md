
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

- Arash_Hosseini.jpg (73.4 KB)
- asphalt material research.jpg (60.9 KB)
- asphalt samples.webp (43.8 KB)
- deep foundation design.jpg (186.8 KB)
- Dr Ahmed Abdalla.jpeg (137.5 KB)
- drill rig.jpg (8.2 KB)
- geotechnical and geo structural.jpg (45.9 KB)
- levee assessment.webp (354.2 KB)
- pavement and material (capabilities).jpg (14.9 KB)
- pavement performance study.jpg (28.0 KB)
- road rehabilitation.jpg (524.7 KB)
- soil improvement.webp (71.3 KB)
- solar and BESS design.webp (233.8 KB)
- transportation and roadway.jpg (9.0 KB)
