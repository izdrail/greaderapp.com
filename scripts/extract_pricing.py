import os
import re
from bs4 import BeautifulSoup

def read_file(path):
    with open(path, 'r') as f: return f.read()
def write_file(path, content):
    with open(path, 'w') as f: f.write(content)

pricing_html = read_file('src/pages/pricing.astro')
soup = BeautifulSoup(pricing_html, 'html.parser')

cards = soup.find_all('div', class_='col-12 col-md-6 col-lg-4')
if cards:
    # Let's extract the first pricing card HTML and make it a component
    card_html = str(cards[0])
    
    # We will just write a simple PricingCard component template
    comp = """---
const { title, price, period, features = [], isFeatured = False } = Astro.props;
---
<div class="col-12 col-md-6 col-lg-4">
    <div class={`price-plan ${isFeatured ? 'featured' : ''} text-center`}>
        <div class="plan-title mb-4">
            <h4 class="mt-0 mb-2">{title}</h4>
        </div>
        <div class="plan-price mb-4">
            <h2 class="mt-0 mb-0"><span>$</span>{price}</h2>
            <span class="plan-period">{period}</span>
        </div>
        <ul class="plan-features list-unstyled mb-4">
            {features.map(f => (
                <li class={f.active ? '' : 'text-muted'}>{f.text}</li>
            ))}
        </ul>
        <div class="plan-button">
            <a href="#" class="btn mt-4">Select Plan</a>
        </div>
    </div>
</div>
"""
    write_file('src/components/PricingCard.astro', comp)

