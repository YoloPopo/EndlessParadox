import re
from pathlib import Path
p=Path(r"d:\Thesis\thesis topics\Thesis\Thesis Progress\latest draft.tex")
src=p.read_text(encoding='utf-8')
lines=src.splitlines()
# find existing subsubsec labels
existing=set(re.findall(r"\\label\{subsubsec:([a-zA-Z0-9_\-]+)\}",src))
# helper
def sanitize(s):
    s=re.sub(r"\\\\[a-zA-Z]+\*?\{.*?\}","",s)
    s=re.sub(r"[^0-9a-zA-Z]+","_",s)
    s=re.sub(r"_+","_",s)
    s=s.strip("_")
    s=s.lower()
    if not s: s='unnamed'
    base=s
    i=1
    while s in existing:
        s=f"{base}_{i}"
        i+=1
    existing.add(s)
    return s

out=[]
i=0
while i<len(lines):
    line=lines[i]
    out.append(line)
    m=re.match(r"^(\s*)\\subsubsection\{(.*)\}",line)
    if m:
        has_label=False
        for j in range(1,6):
            if i+j>=len(lines): break
            nxt=lines[i+j].strip()
            if nxt=="": continue
            if re.match(r"\\label\{",nxt):
                has_label=True
                break
            if re.match(r"^(\\subsubsection|\\subsection|\\section|\\chapter)\b",nxt):
                break
        if not has_label:
            title=m.group(2)
            lab=sanitize(title)
            labline=f"\\label{{subsubsec:{lab}}}"
            out.append(labline)
    i+=1
new='\n'.join(out)
# backup handled earlier; overwrite file
p.write_text(new,encoding='utf-8')
print('Inserted subsubsection labels where missing')
