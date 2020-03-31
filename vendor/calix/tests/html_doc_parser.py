import re
# Run text through the FSM.
# The argument 'template' is a file handle and 'raw_text_data' is a string.
with open("../docs/c7tl1/C7Tl1.html", 'r') as f:
    read_html = f.read()

regex = re.findall(r"<H3>Input Format</H3>[\s\S]*<PRE><CODE>\s([\s\S]*)<\\/CODE>", read_html)
print(regex)
