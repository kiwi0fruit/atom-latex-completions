import re
import os.path as p

with open(p.join('.', '__completions.json'), 'r', encoding='utf-8') as f:
    src = f.read()

numbers = dict(zero=0, one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)
others = dict(ltphi=r'phi\\lt', pgamma=r'gamma\\phon', pbgam=r'gamma\\phon2', ltlmr=r'r\\ltl',
              imath=r'i\\math', jmath=r'j\\math', itimath=r'i\\itmath', itjmath=r'j\\itmath',
              bigamma=r'gamma\\bi', big=r'g\\bi', bfiota=r'iota\\bf',
              sansLturned=r'L\\rot\\sans', sansLmirrored=r'L\\mirr\\sans')

src = re.sub(f'"({"|".join(map(re.escape, others.keys()))})": "',
             lambda m: f'"{others.get(m.group(1))}": "',
             src)

src = re.sub(
    r'"(b?frak|b?i?sans(?:var)?|[bm]?scr|it(?:var)?|bbi?|bf(?:var)?|bivar|bi(?!g)|tt|rtl|ltl)(\w+)": "',
    lambda m: rf'"{numbers.get(m.group(2), m.group(2))}\\{m.group(1)}": "',
    src)

with open(p.join('.', 'completions.json'), 'w', encoding='utf-8') as f:
    f.write(src)
