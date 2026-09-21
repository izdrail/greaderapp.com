import os
import re
from bs4 import BeautifulSoup, Comment

pages_dir = 'src/pages'
components_dir = 'src/components'
layouts_dir = 'src/layouts'

def read_file(path):
    with open(path, 'r') as f: return f.read()

def write_file(path, content):
    with open(path, 'w') as f: f.write(content)

# 1. Extract Header and Footer from BaseLayout or index.astro
index_content = read_file(f'{pages_dir}/index.astro')

header_match = re.search(r'(<!-- \*\*\*\*\* Header Start \*\*\*\*\* -->.*?<!-- \*\*\*\*\* Header End \*\*\*\*\* -->)', index_content, re.DOTALL)
if header_match:
    header_html = header_match.group(1)
    write_file(f'{components_dir}/Header.astro', f'---\n---\n{header_html}')
else:
    print("Header not found")

footer_match = re.search(r'(<!--====== Footer Area Start ======-->.*?<!--====== Footer Area End ======-->)', index_content, re.DOTALL)
if footer_match:
    footer_html = footer_match.group(1)
    write_file(f'{components_dir}/Footer.astro', f'---\n---\n{footer_html}')
else:
    print("Footer not found")

# Replace in all pages
import glob
for filepath in glob.glob(f'{pages_dir}/*.astro'):
    content = read_file(filepath)
    
    # Import Header/Footer if not present
    if 'import Header' not in content:
        content = re.sub(r'(---.*?)(---)', r'\1import Header from "../components/Header.astro";\nimport Footer from "../components/Footer.astro";\n\2', content, flags=re.DOTALL, count=1)
    
    # Replace header HTML
    content = re.sub(r'<!-- \*\*\*\*\* Header Start \*\*\*\*\* -->.*?<!-- \*\*\*\*\* Header End \*\*\*\*\* -->', '<Header />', content, flags=re.DOTALL)
    
    # Replace footer HTML
    content = re.sub(r'<!--====== Footer Area Start ======-->.*?<!--====== Footer Area End ======-->', '<Footer />', content, flags=re.DOTALL)

    write_file(filepath, content)

# Also update BaseLayout to include Header and Footer if they are there, wait, BaseLayout doesn't have Header/Footer, they are in the pages right now!
# Let's move Header and Footer to BaseLayout!
base_content = read_file(f'{layouts_dir}/BaseLayout.astro')
if '<Header />' not in base_content:
    base_content = base_content.replace('<slot />', '<Header />\n    <slot />\n    <Footer />')
    base_content = base_content.replace('---', '---\nimport Header from "../components/Header.astro";\nimport Footer from "../components/Footer.astro";\n', 1)
    write_file(f'{layouts_dir}/BaseLayout.astro', base_content)

# Since we moved them to BaseLayout, we should remove them from all pages to avoid duplication
for filepath in glob.glob(f'{pages_dir}/*.astro'):
    content = read_file(filepath)
    content = content.replace('<Header />', '')
    content = content.replace('<Footer />', '')
    # Also remove the unused imports
    content = content.replace('import Header from "../components/Header.astro";\n', '')
    content = content.replace('import Footer from "../components/Footer.astro";\n', '')
    write_file(filepath, content)

