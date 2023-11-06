import requests as req
import math
from tqdm import tqdm
import time
print("name")
response=req.get("https://djjs.org")
print(response.text)
chunk_size=256
url="https://www.pdf995.com/samples/pdf.pdf"
r=req.get(url)
s=int(r.headers['Content-Length'])
r=req.get(url,stream=True)
n=math.ceil(s/chunk_size)
with open("file.pdf","wb") as file:
    for chunk in tqdm(r.iter_content(chunk_size=chunk_size),total=n):
        file.write(chunk)