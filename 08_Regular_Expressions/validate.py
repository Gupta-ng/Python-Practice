"""
email = input("what's your email? ").strip()
if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")
"""
"""
email = input("what's your email? ").strip()
username, domain = email.split("@")
if username and "." in domain:
    print("valid")
else:
    print("invalid")
"""
"""    
email = input("what's your email? ").strip()
username, domain = email.split("@")
if username and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")
"""
"""
import re
email = input("what's your email? ").strip()
if re.search("@", email):
    print("valid")
else:
    print("invalid")
"""
"""
import re
email = input("what's your email? ").strip()
if re.search(".*@.*", email):
    print("valid")
else:
    print("invalid")
"""
"""
import re
email = input("what's your email? ").strip()
if re.search(r".+@.+\.edu", email):
    print("valid")
else:
    print("invalid")
"""
"""
import re
email = input("what's your email? ").strip()
if re.search(r"^.+@.+\.edu$", email):
    print("valid")
else:
    print("invalid")
"""
"""
import re
email = input("what's your email? ").strip()
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("valid")
else:
    print("invalid")
"""
"""
import re
email = input("what's your email? ").strip()
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("valid")
else:
    print("invalid")
"""
"""
import re
email = input("what's your email? ").strip()
if re.search(r"^[\w.]+@\w+\.(edu|com)$", email):
    print("valid")
else:
    print("invalid")
"""
"""
import re
email = input("what's your email? ").strip()
if re.search(r"^[\w.]+@\w+\.(edu|com)$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")
"""
"""
import re
email = input("what's your email? ").strip()
if re.search(r"^\w+@(\w+.)?\w+\.(edu|com)$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")
"""

import re
email = input("what's your email? ").strip()
if re.search(r"^(\w|\.)+@(\w+.)?\w+\.(edu|com)$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid") 


