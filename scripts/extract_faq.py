import os
import re
from bs4 import BeautifulSoup

def read_file(path):
    with open(path, 'r') as f: return f.read()
def write_file(path, content):
    with open(path, 'w') as f: f.write(content)

faq_html = read_file('src/pages/faq.astro')
soup = BeautifulSoup(faq_html, 'html.parser')

# Find FAQ items (usually inside accordion or just cards)
faq_items = soup.find_all('div', class_='card')

if faq_items:
    # Just take the HTML of the first card as template
    first_item = str(faq_items[0])
    
    comp = """---
const { id, title, content, parentId, expanded = false } = Astro.props;
---
<div class="card border-0">
    <!-- Card Header -->
    <div class="card-header bg-transparent p-0 border-0" id={`heading${id}`}>
        <h2 class="mb-0">
            <button class={`btn px-0 py-3 ${expanded ? '' : 'collapsed'}`} type="button" data-bs-toggle="collapse" data-bs-target={`#collapse${id}`} aria-expanded={expanded ? 'true' : 'false'} aria-controls={`collapse${id}`}>
                {title}
            </button>
        </h2>
    </div>
    <!-- Card Body -->
    <div id={`collapse${id}`} class={`collapse ${expanded ? 'show' : ''}`} aria-labelledby={`heading${id}`} data-bs-parent={`#${parentId}`}>
        <div class="card-body pt-0">
            {content}
        </div>
    </div>
</div>
"""
    write_file('src/components/FaqItem.astro', comp)
    
