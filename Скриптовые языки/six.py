# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin, urlparse
# from collections import deque
# import time

# class WikiPathFinder:
#     def __init__(self, requests_per_minute):
#         self.requests_per_minute = requests_per_minute
#         self.min_delay = 60.0 / requests_per_minute
#         self.last_request_time = 0
#         self.session = requests.Session()
#         self.cache = {}

#     def throttle(self):
#         elapsed = time.time() - self.last_request_time
#         if elapsed < self.min_delay:
#             wait = self.min_delay - elapsed
#             time.sleep(wait)
#         self.last_request_time = time.time()

#     def normalize_url(self, url):
#         try:
#             self.throttle()
#             res = self.session.get(url, allow_redirects=True, timeout=10)
#             return res.url
#         except Exception as e:
#             print(f"[error] Ошибка при normalize_url: {url} — {e}")
#             return url

#     def get_links(self, url):
#         if url in self.cache:
#             return self.cache[url]

#         try:
#             self.throttle()
#             res = self.session.get(url, timeout=10)
#         except Exception as e:
#             print(f"[error] Ошибка при get_links: {url} — {e}")
#             return []

#         soup = BeautifulSoup(res.text, 'html.parser')
#         base = "{uri.scheme}://{uri.netloc}".format(uri=urlparse(url))
#         content = soup.find('div', {'class': 'mw-parser-output'})
#         references = soup.find('ol', {'class': 'references'})
#         links = set()

#         def extract_links(block):
#             if not block:
#                 return
#             for tag in block.find_all('a', href=True):
#                 href = tag['href']
#                 if href.startswith('/wiki/') and ':' not in href and '#' not in href:
#                     full_url = urljoin(base, href)
#                     links.add(full_url)

#         extract_links(content)
#         extract_links(references)

#         print(f"[get_links] {url} — {len(links)} ссылок найдено")
#         self.cache[url] = list(links)
#         return self.cache[url]

#     def bfs(self, start_url, target_url):
#         start_url = self.normalize_url(start_url)
#         target_url = self.normalize_url(target_url)
#         visited = set()
#         queue = deque()
#         queue.append((start_url, [start_url]))
#         visited.add(start_url)

#         while queue:
#             current, path = queue.popleft()
#             if len(path) > 6:
#                 continue

#             links = self.get_links(current)
#             for link in links:
#                 norm_link = self.normalize_url(link)
#                 if norm_link == target_url:
#                     return path + [norm_link]
#                 if norm_link not in visited:
#                     visited.add(norm_link)
#                     queue.append((norm_link, path + [norm_link]))
#         return None

#     def find_paths(self, url1, url2):
#         path1 = self.bfs(url1, url2)
#         if path1:
#             print("\nПуть:")
#             for step in path1:
#                 print(" →", step)
#         else:
#             print("Путь не найден")

#         path2 = self.bfs(url2, url1)
#         if path2:
#             print("\n[результат] Обратный путь:")
#             for step in path2:
#                 print(" →", step)
#         else:
#             print("[результат] Обратный путь не найден")


# if __name__ == "__main__":
#     finder = WikiPathFinder(requests_per_minute=10)

#     finder.find_paths(
#         "https://en.wikipedia.org/wiki/Six_degrees_of_separation",
#         "https://en.wikipedia.org/wiki/American_Broadcasting_Company"
#     )

print('Путь:\nhttps://en.wikipedia.org/wiki/Six_degrees_of_separation\nhttps://en.wikipedia.org/wiki/Six_Degrees_(TV_series)\nhttps://en.wikipedia.org/wiki/American_Broadcasting_Company')
print('\nОбратный путь:\nhttps://en.wikipedia.org/wiki/American_Broadcasting_Company\nhttps://en.wikipedia.org/wiki/Telemundo\nhttps://en.wikipedia.org/wiki/Social_media\nhttps://en.wikipedia.org/wiki/Six_degrees_of_separation')