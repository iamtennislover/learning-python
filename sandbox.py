# sandbox
import hashlib, base64
text = "www.yahoo.com"
text_utf8 = text.encode('utf8')
md5 = hashlib.md5(text_utf8).digest()
b64 = base64.b64encode(md5)
print(b64)
print(md5)
print(base64.b64encode(b"www.yahoo.com"))
