import os
import re
from bs4 import BeautifulSoup

def read_file(path):
    with open(path, 'r') as f: return f.read()
def write_file(path, content):
    with open(path, 'w') as f: f.write(content)

review_html = read_file('src/pages/reviews.astro')
soup = BeautifulSoup(review_html, 'html.parser')

reviews = soup.find_all('div', class_='single-review')

if reviews:
    comp = """---
const { name, text, image, stars = 5, platform = "Google" } = Astro.props;
---
<div class="single-review card">
    <!-- Card Top -->
    <div class="card-top p-4">
        <div class="review-icon">
            <i class="fas fa-star text-warning"></i>
            <i class="fas fa-star text-warning"></i>
            <i class="fas fa-star text-warning"></i>
            <i class="fas fa-star text-warning"></i>
            <i class="fas fa-star text-warning"></i>
        </div>
        <h4 class="text-primary mt-4 mb-3">{name}</h4>
        <div class="review-text">
            <p>{text}</p>
        </div>
        <!-- Quotation Icon -->
        <div class="quot-icon">
            <img class="avatar-md" src="/assets/img/icon/quote.png" alt="" />
        </div>
    </div>
    <!-- Reviewer -->
    <div class="reviewer media bg-gray p-4">
        <div class="reviewer-thumb">
            <img class="avatar-lg radius-100" src={image} alt="" />
        </div>
        <div class="reviewer-meta media-body align-self-center ml-4">
            <h5 class="reviewer-name color-primary mb-2">{name}</h5>
            <h6 class="text-secondary fw-6">{platform}</h6>
        </div>
    </div>
</div>
"""
    write_file('src/components/ReviewCard.astro', comp)
    
