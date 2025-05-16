import re

def scrub_text(text):
    # html tags
    text = re.sub(r'<[^>]+>', '', text)

    # email addresses
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)

    # for urls
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    return text
