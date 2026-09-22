import os
import glob
import re

design_dir = 'design'
pages_dir = 'src/pages'
layouts_dir = 'src/layouts'
components_dir = 'src/components'

os.makedirs(pages_dir, exist_ok=True)
os.makedirs(layouts_dir, exist_ok=True)
os.makedirs(components_dir, exist_ok=True)

# Generate BaseLayout
base_layout = """---
const { title = "greaderapp.com - Modern, privacy-respecting RSS/news reader" } = Astro.props;
---
<!doctype html>
<html class="no-js" lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="description" content="greaderapp.com - The open-source version of the old gReader news app.">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{title}</title>
    <link rel="icon" href="/assets/img/favicon.png">
    <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
    <slot />
    
    <!-- ***** All jQuery Plugins ***** -->
    <!-- jQuery(necessary for all JavaScript plugins) -->
    <script is:inline src="/assets/js/vendor/jquery.min.js"></script>
    <!-- Bootstrap js -->
    <script is:inline src="/assets/js/vendor/popper.min.js"></script>
    <script is:inline src="/assets/js/vendor/bootstrap.min.js"></script>
    <!-- Plugins js -->
    <script is:inline src="/assets/js/vendor/all.min.js"></script>
    <!-- Slider js -->
    <script is:inline src="/assets/js/vendor/slider.min.js"></script>
    <!-- Countdown js -->
    <script is:inline src="/assets/js/vendor/countdown.min.js"></script>
    <!-- Counterup js -->
    <script is:inline src="/assets/js/vendor/counterup.js"></script>
    <!-- AOS js -->
    <script is:inline src="/assets/js/vendor/aos.js"></script>
    <!-- WOW js -->
    <script is:inline src="/assets/js/vendor/wow.min.js"></script>
    <!-- Waypoint js -->
    <script is:inline src="/assets/js/vendor/waypoint.js"></script>
    <!-- Active js -->
    <script is:inline src="/assets/js/main.js"></script>
</body>
</html>
"""
with open(f'{layouts_dir}/BaseLayout.astro', 'w') as f:
    f.write(base_layout)

html_files = glob.glob(f'{design_dir}/*.html')

for filepath in html_files:
    filename = os.path.basename(filepath)
    name, _ = os.path.splitext(filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract body content (very simplistically for now)
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.IGNORECASE | re.DOTALL)
    
    if body_match:
        body_content = body_match.group(1)
        
        # Remove script tags that are moved to BaseLayout
        body_content = re.sub(r'<script.*?src="assets/js/.*?></script>', '', body_content, flags=re.IGNORECASE | re.DOTALL)
        # Fix asset paths
        body_content = body_content.replace('"assets/', '"/assets/')
        body_content = body_content.replace("'assets/", "'/assets/")
        
        # Some app name updates
        body_content = body_content.replace('sApp', 'gReader News')
        
        astro_content = f"""---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="{name} - greaderapp.com">
{body_content}
</BaseLayout>
"""
        with open(f'{pages_dir}/{name}.astro', 'w', encoding='utf-8') as f:
            f.write(astro_content)

