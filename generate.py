def generate_css() -> list:
    with open("malicious links", "r") as f:
        links = f.read().split("\n")
    
    for link in links:
        if link:
            links[links.index(link)] = f"[href^='{link}']"
    
    return links

def write_import_file() -> None:
    with open("template.min.css", "r") as f:
        template = f.read()

    links = generate_css()

    with open("import.css", "w") as f:
        f.write(template.replace("$$links$$", ",".join(links)))

write_import_file()
    
