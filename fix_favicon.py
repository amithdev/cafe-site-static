import glob
import re

new_favicon_block = """<link rel="icon" href="https://www.breadsandbanter.com/favicon.ico" sizes="48x48">
<link rel="icon" href="https://www.breadsandbanter.com/bnb-favicon.png" type="image/png" sizes="96x96">
<link rel="apple-touch-icon" href="https://www.breadsandbanter.com/apple-touch-icon.png">"""

html_files = glob.glob("**/*.html", recursive=True)
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will use regex to find the block of favicon tags
    # The block starts with <link rel="icon" type="image/png" and ends with <link rel="manifest" ... >
    
    # We'll match all link tags that are about icons or manifests and replace them
    pattern = re.compile(r'(<link[^>]+(?:icon|manifest)[^>]*>\s*)+', re.IGNORECASE)
    
    content = pattern.sub(new_favicon_block + '\n', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
