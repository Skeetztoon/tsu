import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import time

def extract_links(url, lang_prefix):
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = set()
        content = soup.find("div", class_="mw-parser-output")

        for tag in content.find_all("a", href=True):
            href = tag['href']
            if href.startswith('/wiki/') and not any(x in href for x in [':', '#']):
                full_url = urljoin("https://" + lang_prefix + ".wikipedia.org", href)
                links.add(full_url)

        return list(links)
    except Exception:
        return []

def limited_get(url, lang_prefix, state):
    while state['requests'] >= state['limit']:
        if time.time() - state['start'] >= 60:
            state['requests'] = 0
            state['start'] = time.time()
        else:
            time.sleep(1)
    state['requests'] += 1
    return extract_links(url, lang_prefix)

def bfs(url1, url2, limit):
    lang = urlparse(url1).netloc.split('.')[0]
    state = {'requests': 0, 'limit': limit, 'start': time.time()}

    if url1 == url2:
        return [url1]

    queue_f, queue_b = deque([url1]), deque([url2])
    visited_f, visited_b = {url1: None}, {url2: None}

    for depth in range(5):
        for _ in range(len(queue_f)):
            node = queue_f.popleft()
            for link in limited_get(node, lang, state):
                if link not in visited_f:
                    visited_f[link] = node
                    queue_f.append(link)
                    if link in visited_b:
                        return reconstruct(visited_f, visited_b, link)

        for _ in range(len(queue_b)):
            node = queue_b.popleft()
            for link in limited_get(node, lang, state):
                if link not in visited_b:
                    visited_b[link] = node
                    queue_b.append(link)
                    if link in visited_f:
                        return reconstruct(visited_f, visited_b, link)

    return None

def reconstruct(fwd, bwd, meet):
    path_fwd, path_bwd = [], []
    node = meet
    while node:
        path_fwd.append(node)
        node = fwd[node]
    path_fwd.reverse()

    node = bwd[meet]
    while node:
        path_bwd.append(node)
        node = bwd[node]

    return path_fwd + path_bwd


url1 = "https://en.wikipedia.org/wiki/Ghalib_Academy,_New_Delhi"
url2 = "https://en.wikipedia.org/wiki/Walter_Melrose"
limit = 10

path1 = bfs(url1, url2, limit)
path2 = bfs(url2, url1, limit)

def format_path(path, start, end):
    if not path:
        return f"No path found between {start} and {end} within 5 hops"
    return " => ".join(path)

print("url1 => url2:")
print(format_path(path1, url1, url2))
print("\nurl2 => url1:")
print(format_path(path2, url2, url1))
