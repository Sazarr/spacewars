import re
def domain_name(url):
    return re.search(r"(?:https?://)?(?:www\.)?([^./]+)", url).group(1)

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]