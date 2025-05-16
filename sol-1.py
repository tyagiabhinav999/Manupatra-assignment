import re

def scrub_text(text):
    # html tags
    text = re.sub(r'<[^>]+>', '', text)

    # email addresses
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)

    # for urls
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    return text

sample = """
<p>paragraph with an <a href="http://example.com"> link</a>.</p>
something hi@example.com website www.xyz.com.
<div>html <b>bold text</b> and div </div>
blablabla is https://sub.domain.com/path?query=value.
"""

out = scrub_text(sample)


print(out)

### Output is

# PS D:\ManuPatra> python sol-1.py
# paragraph with an  link.
# something  website
# html bold text and div
# blablabla is