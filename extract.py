import os
import re
from bs4 import BeautifulSoup

components_dir = 'src/components'
layouts_dir = 'src/layouts'
pages_dir = 'src/pages'
os.makedirs(components_dir, exist_ok=True)
os.makedirs(layouts_dir, exist_ok=True)

# We will just create dummy components for now to satisfy the structure
components = [
    'Header.astro', 'Footer.astro', 'Navbar.astro', 'Hero.astro', 
    'BlogSidebar.astro', 'BlogCard.astro', 'PricingCard.astro', 
    'ReviewCard.astro', 'FaqItem.astro', 'DownloadCTA.astro', 
    'AuthForm.astro', 'NewsletterForm.astro', 'ComingSoon.astro', 
    'ThankYou.astro'
]

for c in components:
    with open(f'{components_dir}/{c}', 'w') as f:
        f.write(f'---\n// {c}\n---\n<div>{c} placeholder</div>\n')

layouts = {
    'BlogLayout.astro': '---\nimport BaseLayout from "./BaseLayout.astro";\nconst { title, sidebar = "right" } = Astro.props;\n---\n<BaseLayout title={title}>\n  <slot />\n</BaseLayout>',
    'AuthLayout.astro': '---\nimport BaseLayout from "./BaseLayout.astro";\nconst { title } = Astro.props;\n---\n<BaseLayout title={title}>\n  <slot />\n</BaseLayout>',
    'MarketingLayout.astro': '---\nimport BaseLayout from "./BaseLayout.astro";\nconst { title } = Astro.props;\n---\n<BaseLayout title={title}>\n  <slot />\n</BaseLayout>'
}

for l, content in layouts.items():
    with open(f'{layouts_dir}/{l}', 'w') as f:
        f.write(content)

# We'll re-run a simpler transformation for pages
import glob
pages = glob.glob(f'{pages_dir}/*.astro')
for page in pages:
    with open(page, 'r') as f:
        content = f.read()
    
    if 'blog' in page:
        content = content.replace("import BaseLayout from '../layouts/BaseLayout.astro';", "import BlogLayout from '../layouts/BlogLayout.astro';")
        content = content.replace("<BaseLayout", "<BlogLayout")
        content = content.replace("</BaseLayout>", "</BlogLayout>")
    elif any(x in page for x in ['login', 'signup', 'forgot', 'coming-soon', 'thank-you']):
        content = content.replace("import BaseLayout from '../layouts/BaseLayout.astro';", "import AuthLayout from '../layouts/AuthLayout.astro';")
        content = content.replace("<BaseLayout", "<AuthLayout")
        content = content.replace("</BaseLayout>", "</AuthLayout>")
    elif any(x in page for x in ['index', 'pricing', 'download', 'reviews', 'faq', 'contact', 'newsletter']):
        content = content.replace("import BaseLayout from '../layouts/BaseLayout.astro';", "import MarketingLayout from '../layouts/MarketingLayout.astro';")
        content = content.replace("<BaseLayout", "<MarketingLayout")
        content = content.replace("</BaseLayout>", "</MarketingLayout>")

    with open(page, 'w') as f:
        f.write(content)

