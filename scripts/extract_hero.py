import os
import re
from bs4 import BeautifulSoup

def read_file(path):
    with open(path, 'r') as f: return f.read()
def write_file(path, content):
    with open(path, 'w') as f: f.write(content)

pages_dir = 'src/pages'
index_html = read_file(f'{pages_dir}/index.astro')

hero_match = re.search(r'(<!-- \*\*\*\*\* Hero Section Start \*\*\*\*\* -->.*?<!-- \*\*\*\*\* Hero Section End \*\*\*\*\* -->)', index_html, re.DOTALL)
if hero_match:
    hero_html = hero_match.group(1)
    
    # Generate Hero component
    hero_comp = f'---\n---\n{hero_html}'
    write_file('src/components/Hero.astro', hero_comp)
    
    # Replace in index.astro
    index_html = index_html.replace(hero_html, '<Hero />')
    if 'import Hero from' not in index_html:
        index_html = index_html.replace('---', '---\nimport Hero from "../components/Hero.astro";\n', 1)
    write_file(f'{pages_dir}/index.astro', index_html)

