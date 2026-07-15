"""
url = input("URL: ").strip()
print(url)
"""

"""
url = input("URL: ").strip()
username = url.replace("https://twitter.com/", "")
print(f"username: {username}")
"""

"""
url = input("URL: ").strip()
username = url.removeprefix("https://twitter.com/")
print(f"username: {username}")
"""
"""
import re
url = input("URL: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"username: {username}")
"""

"""
import re
url = input("URL: ").strip()
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"username:", matches.group(2))
"""
"""
import re
url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
     print(f"username:", matches.group(1))
"""
import re
url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
     print(f"username:", matches.group(1))


 

