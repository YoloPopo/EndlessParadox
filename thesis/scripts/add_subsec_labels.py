import re
from pathlib import Path
p=Path(r"d:\Thesis\thesis topics\Thesis\Thesis Progress\latest draft.tex")
src=p.read_text(encoding='utf-8')
lines=src.splitlines()
# find existing subsec labels
existing_labels=set(re.findall(r"\\label\{subsec:([a-zA-Z0-9_\-]+)\}",src))
# helper to sanitize title
def sanitize(s):
    s=re.sub(r"\\\\[a-zA-Z]+\*?\{.*?\}","",s) # remove simple LaTeX commands
    s=re.sub(r"[^0-9a-zA-Z]+","_",s)
    s=re.sub(r"_+","_",s)
    s=s.strip("_")
    s=s.lower()
    if not s: s='unnamed'
    base=s
    i=1
    while s in existing_labels:
        s=f"{base}_{i}"
        i+=1
    existing_labels.add(s)
    return s

out_lines=[]
i=0
while i < len(lines):
    line=lines[i]
    out_lines.append(line)
    m=re.match(r"^(\s*)\\subsection\{(.*)\}",line)
    if m:
        # look ahead for up to 4 non-empty lines to see if a label exists
        has_label=False
        for j in range(1,6):
            if i+j>=len(lines): break
            nxt=lines[i+j].strip()
            if nxt=="":
                continue
            if nxt.startswith('%'):
                continue
            if re.match(r"\\label\{",nxt):
                has_label=True
                break
            # if next is another \subsection or \section or \chapter then stop
            if re.match(r"^(\\subsection|\\section|\\chapter)\b",nxt):
                break
        if not has_label:
            title=m.group(2)
            lab=sanitize(title)
            label_line=f"\\label{{subsec:{lab}}}"
            out_lines.append(label_line)
    i+=1

new_text='\n'.join(out_lines)
# backup
bak=p.with_suffix('.tex.bak')
if not bak.exists():
    p.rename(bak)
    p.write_text(new_text,encoding='utf-8')
    print('Rewrote file; backup created at',str(bak))
else:
    # if backup already existed, overwrite original from backup and then write
    p.write_text(new_text,encoding='utf-8')
    print('Rewrote file; backup already existed, original overwritten')
