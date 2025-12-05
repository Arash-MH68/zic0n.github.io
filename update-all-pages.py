#!/usr/bin/env python3
"""
Script to update all HTML pages with improved styles and scripts
"""

import os
import re

# List of HTML files to update
html_files = [
    'about.html',
    'services.html',
    'contact.html',
    'leadership.html',
    'projects.html',
    'markets.html',
    'capabilities.html',
    'approach.html',
    'faqs.html',
    'newsletter.html'
]

def update_html_file(filename):
    """Update a single HTML file with improvements"""
    print(f"Updating {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update resource loading (remove defer, add preconnect)
    content = re.sub(
        r'<script src="https://cdn\.tailwindcss\.com" defer></script>',
        '<script src="https://cdn.tailwindcss.com"></script>',
        content
    )
    
    content = re.sub(
        r'<script src="https://unpkg\.com/feather-icons" defer></script>',
        '<script src="https://unpkg.com/feather-icons"></script>',
        content
    )
    
    # 2. Add external CSS link before </head>
    if 'styles.css' not in content:
        content = re.sub(
            r'(<script src="https://unpkg\.com/feather-icons"></script>)',
            r'\1\n  \n  <!-- ======= Custom Styles ======= -->\n  <link rel="stylesheet" href="styles.css">',
            content
        )
    
    # 3. Add DNS prefetch hints
    if 'dns-prefetch' not in content:
        content = re.sub(
            r'(<link rel="preconnect" href="https://fonts\.googleapis\.com">)',
            r'<!-- ======= Preload Critical Resources ======= -->\n  <link rel="preconnect" href="https://cdn.tailwindcss.com">\n  <link rel="dns-prefetch" href="https://unpkg.com">\n  \1',
            content
        )
    
    # 4. Remove inline styles
    content = re.sub(
        r'  <style>.*?</style>\n',
        '',
        content,
        flags=re.DOTALL
    )
    
    # 5. Update mobile menu button with better ARIA
    content = re.sub(
        r'<button id="menuBtn" class="md:hidden p-2 rounded hover:bg-white/10" aria-label="Open menu">',
        '<button id="menuBtn" class="md:hidden p-2 rounded hover:bg-white/10 transition" aria-label="Open menu" aria-expanded="false" aria-controls="mobileMenu">',
        content
    )
    
    # 6. Add role to mobile menu
    content = re.sub(
        r'<div id="mobileMenu" class="md:hidden hidden border-t border-white/10">',
        '<div id="mobileMenu" class="md:hidden hidden border-t border-white/10" role="navigation" aria-label="Mobile navigation">',
        content
    )
    
    # 7. Replace inline JavaScript with external script
    content = re.sub(
        r'  <script>.*?</script>\n\n  <!-- ======= JSON-LD',
        r'  <!-- ======= Back to Top Button ======= -->\n  <button id="backToTop" class="back-to-top no-print" aria-label="Back to top">\n    <i data-feather="arrow-up"></i>\n  </button>\n\n  <!-- ======= Custom JavaScript ======= -->\n  <script src="app.js"></script>\n\n  <!-- ======= JSON-LD',
        content,
        flags=re.DOTALL
    )
    
    # If no JSON-LD, just replace before </body>
    if '<!-- ======= JSON-LD' not in content:
        content = re.sub(
            r'  <script>.*?</script>\n</body>',
            r'  <!-- ======= Back to Top Button ======= -->\n  <button id="backToTop" class="back-to-top no-print" aria-label="Back to top">\n    <i data-feather="arrow-up"></i>\n  </button>\n\n  <!-- ======= Custom JavaScript ======= -->\n  <script src="app.js"></script>\n</body>',
            content,
            flags=re.DOTALL
        )
    
    # 8. Add hover effects to buttons and links
    content = re.sub(
        r'class="(.*?px-\d+ py-\d+.*?rounded.*?)"',
        lambda m: f'class="{m.group(1)} transition transform hover:scale-105"' if 'transition' not in m.group(1) else m.group(0),
        content
    )
    
    # Write updated content
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {filename}")

def main():
    """Main function to update all HTML files"""
    print("Starting HTML file updates...\n")
    
    for filename in html_files:
        if os.path.exists(filename):
            try:
                update_html_file(filename)
            except Exception as e:
                print(f"✗ Error updating {filename}: {e}")
        else:
            print(f"⚠ File not found: {filename}")
    
    print("\n✓ All files updated successfully!")

if __name__ == '__main__':
    main()
