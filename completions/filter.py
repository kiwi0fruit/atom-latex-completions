import re
import os.path as p

with open(p.join('.', '__completions.json'), 'r', encoding='utf-8') as f:
    src = f.read()

numbers = dict(zero=0, one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)

src = re.sub(r'"(b?frak|b?i?sans|[bm]?scr|itvar|it|b[bif]|tt|rtl|ltl)(\w+)": "',
             lambda m: rf'"{numbers.get(m.group(2), m.group(2))}\\{m.group(1)}": "',
             src.replace('"ltphi"', r'"phi\\lt"'
                         ).replace('"pgamma"', r'"gamma\\phon"'
                                   ).replace('"pbgam"', r'"gamma\\phon2"'
                                             ).replace('"ltlmr"', r'"r\\ltl"'))
src = re.sub(r'"(it)?(\w+)math": "',
             lambda m: rf'"{m.group(2)}\\{m.group(1) if m.group(1) else ""}math": "',
             src)

with open(p.join('.', 'completions.json'), 'w', encoding='utf-8') as f:
    f.write(src)
