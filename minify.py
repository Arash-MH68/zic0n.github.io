#!/usr/bin/env python3
"""
Minification script for production deployment
Minifies CSS and JavaScript files
"""

import re
import os
from pathlib import Path

def minify_css(css_content):
    """Minify CSS content"""
    # Remove comments
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    
    # Remove whitespace
    css_content = re.sub(r'\s+', ' ', css_content)
    css_content = re.sub(r'\s*([{}:;,])\s*', r'\1', css_content)
    
    # Remove trailing semicolons
    css_content = re.sub(r';}', '}', css_content)
    
    return css_content.strip()

def minify_js(js_content):
    """Basic JavaScript minification"""
    # Remove single-line comments (but preserve URLs)
    js_content = re.sub(r'(?<!:)//.*?$', '', js_content, flags=re.MULTILINE)
    
    # Remove multi-line comments
    js_content = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)
    
    # Remove extra whitespace
    js_content = re.sub(r'\s+', ' ', js_content)
    js_content = re.sub(r'\s*([{}();,:])\s*', r'\1', js_content)
    
    return js_content.strip()

def process_file(input_path, output_path, file_type):
    """Process and minify a file"""
    print(f"Processing {input_path}...")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if file_type == 'css':
        minified = minify_css(content)
    elif file_type == 'js':
        minified = minify_js(content)
    else:
        minified = content
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(minified)
    
    original_size = len(content)
    minified_size = len(minified)
    savings = ((original_size - minified_size) / original_size) * 100
    
    print(f"  Original: {original_size:,} bytes")
    print(f"  Minified: {minified_size:,} bytes")
    print(f"  Savings: {savings:.1f}%")
    
    return original_size, minified_size

def main():
    """Main function"""
    print("=" * 60)
    print("Production Minification Script")
    print("=" * 60)
    print()
    
    # Create dist directory
    dist_dir = Path('dist')
    dist_dir.mkdir(exist_ok=True)
    
    total_original = 0
    total_minified = 0
    
    # Files to minify
    files_to_process = [
        ('styles.css', 'dist/styles.min.css', 'css'),
        ('app.js', 'dist/app.min.js', 'js'),
        ('contact-form.js', 'dist/contact-form.min.js', 'js'),
        ('analytics.js', 'dist/analytics.min.js', 'js'),
        ('newsletter.js', 'dist/newsletter.min.js', 'js'),
        ('theme-toggle.js', 'dist/theme-toggle.min.js', 'js'),
        ('breadcrumbs.js', 'dist/breadcrumbs.min.js', 'js'),
    ]
    
    for input_file, output_file, file_type in files_to_process:
        if os.path.exists(input_file):
            orig, mini = process_file(input_file, output_file, file_type)
            total_original += orig
            total_minified += mini
            print()
        else:
            print(f"⚠ File not found: {input_file}")
            print()
    
    print("=" * 60)
    print(f"Total Original Size: {total_original:,} bytes")
    print(f"Total Minified Size: {total_minified:,} bytes")
    print(f"Total Savings: {((total_original - total_minified) / total_original) * 100:.1f}%")
    print("=" * 60)
    print()
    print("✓ Minification complete!")
    print()
    print("Next steps:")
    print("1. Update HTML files to use .min.css and .min.js files")
    print("2. Test the minified files")
    print("3. Deploy the dist/ directory to production")

if __name__ == '__main__':
    main()
