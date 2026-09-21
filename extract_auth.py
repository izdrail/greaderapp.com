import os

def write_file(path, content):
    with open(path, 'w') as f: f.write(content)

comp = """---
const { title, subtitle, buttonText, type } = Astro.props;
---
<div class="hero-form">
    <h3 class="mt-0 mb-3">{title}</h3>
    <span>{subtitle}</span>
    <form id="contact-form" class="contact-form mt-3" action="#">
        {type !== 'forgot' && (
            <div class="form-floating mb-3">
                <input type="email" class="form-control" name="email" id="email" placeholder="name@example.com" required>
                <label for="email">Email address</label>
            </div>
        )}
        {(type === 'login' || type === 'signup') && (
            <div class="form-floating mb-3">
                <input type="password" class="form-control" id="password" placeholder="Password" required>
                <label for="password">Password</label>
            </div>
        )}
        <button type="submit" class="btn swap-icon">{buttonText}<i class="icon bi bi-arrow-right-short"></i></button>
    </form>
</div>
"""
write_file('src/components/AuthForm.astro', comp)
    
