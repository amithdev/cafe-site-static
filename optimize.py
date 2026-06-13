import os
import glob

preconnect_tags = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
"""

html_files = glob.glob("**/*.html", recursive=True)
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add preconnect if not already there
    if '<link rel="preconnect"' not in content:
        content = content.replace('<head>', f'<head>{preconnect_tags}')
    
    # Add loading="lazy" to all imgs if not already there
    content = content.replace('<img ', '<img loading="lazy" ')
    # Avoid duplicate loading="lazy" if it was already run
    content = content.replace('<img loading="lazy" loading="lazy"', '<img loading="lazy"')
    
    # Remove loading="lazy" from the logo since it's above the fold
    content = content.replace('<img loading="lazy" src="static/images/logo.png"', '<img src="static/images/logo.png"')
    content = content.replace('<img loading="lazy" src="../static/images/logo.png"', '<img src="../static/images/logo.png"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Done")
