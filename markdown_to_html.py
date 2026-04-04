def markdown_to_html(md_text):
    html = md_text.replace("# ", "<h1>") \
                  .replace("## ", "<h2>") \
                  .replace("**", "<b>") \
                  .replace("*", "<i>")
    return html

if __name__ == "__main__":
    md = input("Enter markdown: ")
    print(markdown_to_html(md))
