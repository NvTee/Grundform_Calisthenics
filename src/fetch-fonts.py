import re, urllib.request, base64
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read()
css=get("https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Barlow:wght@400;500;600;700&display=swap").decode()
blocks=re.findall(r"/\* (\w[\w-]*) \*/\s*@font-face \{(.*?)\}", css, re.S)
out=[]
total=0
for sub, body in blocks:
    if sub!="latin": continue
    fam=re.search(r"font-family: '([^']+)'",body).group(1)
    wt=re.search(r"font-weight: (\d+)",body).group(1)
    url=re.search(r"url\((https://[^)]+)\)",body).group(1)
    data=get(url); total+=len(data)
    b64=base64.b64encode(data).decode()
    out.append("@font-face{font-family:'%s';font-style:normal;font-weight:%s;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}"%(fam,wt,b64))
    print(fam,wt,len(data))
open("fonts.css","w").write("\n".join(out))
print("raw total",total,"css",len(open("fonts.css").read()))
