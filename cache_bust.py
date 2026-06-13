import glob

html_files = glob.glob("**/*.html", recursive=True)
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple replace to add ?v=2
    content = content.replace('href="static/css/style.css"', 'href="static/css/style.css?v=2"')
    content = content.replace('href="../static/css/style.css"', 'href="../static/css/style.css?v=2"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Done")
