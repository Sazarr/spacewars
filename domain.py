import re
def domain_name(url):
    return re.search(r"(?:https?://)?(?:www\.)?([^./]+)", url).group(1)

