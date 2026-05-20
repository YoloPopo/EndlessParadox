import re
from pathlib import Path
p=Path(r"d:\Thesis\thesis topics\Thesis\Thesis Progress\latest draft.tex")
text=p.read_text(encoding='utf-8')
lines=text.splitlines()

# Build heading->label mapping by scanning file and tracking numbering
chap=0; sec=0; subsec=0; subsub=0
mapping={}  # e.g. '3'->'chap:xxx', '3.2'->'sec:xxx', '3.2.1'->'subsec:xxx', '3.2.1.1'->'subsubsec:xxx'

label_regex=re.compile(r"\\label\{([^}]+)\}")

i=0
while i < len(lines):
    line=lines[i]
    chap_m=re.match(r"\\chapter\{", line)
    sec_m=re.match(r"\\section\{", line)
    subsec_m=re.match(r"\\subsection\{", line)
    subsub_m=re.match(r"\\subsubsection\{", line)
    if chap_m:
        chap += 1
        sec=0; subsec=0; subsub=0
        # look for label in same or next 3 non-empty lines
        label=None
        for j in range(i, min(i+5, len(lines))):
            m=label_regex.search(lines[j])
            if m:
                label=m.group(1)
                break
        if label:
            mapping[str(chap)] = label
    elif sec_m:
        sec += 1
        subsec=0; subsub=0
        label=None
        for j in range(i, min(i+5, len(lines))):
            m=label_regex.search(lines[j])
            if m:
                label=m.group(1); break
        if label:
            mapping[f"{chap}.{sec}"] = label
    elif subsec_m:
        subsec += 1
        subsub=0
        label=None
        for j in range(i, min(i+5, len(lines))):
            m=label_regex.search(lines[j])
            if m:
                label=m.group(1); break
        if label:
            mapping[f"{chap}.{sec}.{subsec}"] = label
    elif subsub_m:
        subsub += 1
        label=None
        for j in range(i, min(i+5, len(lines))):
            m=label_regex.search(lines[j])
            if m:
                label=m.group(1); break
        if label:
            mapping[f"{chap}.{sec}.{subsec}.{subsub}"] = label
    i += 1

# report mapping counts
print(f"Found {len([k for k in mapping.keys() if '.' not in k])} chapter labels, {len([k for k in mapping.keys() if k.count('.')==1])} section labels, {len([k for k in mapping.keys() if k.count('.')==2])} subsection labels, {len([k for k in mapping.keys() if k.count('.')==3])} subsubsection labels")

# Backup
bak=p.with_name(p.name + '.bak')
bak.write_text(text, encoding='utf-8')
print(f"Backup written to {bak}")

# Replacement functions
# Replace Chapter ranges like 'Chapters 4–6' or 'Chapters 4-6'

def replace_chapters_range(m):
    start=int(m.group(1)); end=int(m.group(2))
    if str(start) in mapping and str(end) in mapping:
        return f"Chapters~\\ref{{{mapping[str(start)]}}}--\\ref{{{mapping[str(end)]}}}"
    return m.group(0)

# Replace single Chapter
def replace_chapter(m):
    num=int(m.group(1))
    key=str(num)
    if key in mapping:
        return f"Chapter~\\ref{{{mapping[key]}}}"
    return m.group(0)

# Replace Section like 'Section 3.2.3' or '(Section 3.2.3)'
def replace_section(m):
    num=m.group(1)
    if num in mapping:
        return f"Section~\\ref{{{mapping[num]}}}"
    return m.group(0)

# Patterns
pat_chap_range=re.compile(r"Chapters\s+(\d+)[–-](\d+)")
pat_chap=re.compile(r"Chapter\s+(\d+)")
pat_section=re.compile(r"Section\s+(\d+(?:\.\d+){0,3})")

new_text = pat_chap_range.sub(replace_chapters_range, text)
new_text = pat_chap.sub(replace_chapter, new_text)
new_text = pat_section.sub(replace_section, new_text)

# Avoid double-replacing already replaced refs (rudimentary): if '\\ref{' appears immediately after 'Section~' skip
# Write
p.write_text(new_text, encoding='utf-8')

# count diffs
if new_text==text:
    print('No replacements made')
else:
    print('Replacements applied; file updated')
