import re
import os.path as p

with open(p.join('.', '__completions.json'), 'r', encoding='utf-8') as f:
    src = f.read()

numbers = dict(zero=0, one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)
others = dict(ltphi=r'phi\\phon', pgamma=r'gamma\\phon', pbgam=r'gamma\\phon\\', ltlmr=r'r\\phon\\left',
              imath=r'i\\math', jmath=r'j\\math', itimath=r'i\\math\\it', itjmath=r'j\\math\\it',
              bigamma=r'gamma\\bold\\it', big=r'g\\bold\\it', bfiota=r'iota\\bold', upvarbeta=r'beta\\var',
              sansLturned=r'L\\rot\\sans', sansLmirrored=r'L\\mirr\\sans')
styles = dict(bfrak=r'frak\\bold', bsans=r'sans\\bold', isans=r'sans\\it', bisans=r'sans\\bold\\it',
              sansvar=r'var\\sans', bsansvar=r'var\\sans\\bold', isansvar=r'var\\sans\\it',
              bisansvar=r'var\\sans\\bold\\it', bscr=r'scr\\bold', itvar=r'var\\it', bb=r'bbold',
              bbi=r'bbold\\it', bf=r'bold', bfvar=r'var\\bold', bivar=r'var\\bold\\it', bi=r'bold\\it',
              tt=r'mono', rtl=r'phon\\right', ltl=r'phon\\left')

src = re.sub(f'"({"|".join(map(re.escape, others.keys()))})": "',
             lambda m: f'"{others.get(m.group(1))}": "',
             src)

src = re.sub(
    r'"(b?frak|b?i?sans(?:var)?|b?scr|it(?:var)?|bbi?|bf(?:var)?|bivar|bi(?!g)|tt|rtl|ltl|var)(\w+)": "',
    lambda m: rf'"{numbers.get(m.group(2), m.group(2))}\\{styles.get(m.group(1), m.group(1))}": "',
    src)

with open(p.join('.', 'completions.json'), 'w', encoding='utf-8') as f:
    f.write(src)
