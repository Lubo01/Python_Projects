	
# !check string type ASCII or UTF 8 or Unicode to manage non-English characters
"""
You can just check whether the string can be encoded only with ASCII characters
(which are Latin alphabet + some other characters). If it can not be encoded,
then it has the characters from some other alphabet.
Note the comment # -*- coding: ..... It should be there at the top of the python
file (otherwise you would receive some error about encoding).
"""
# -*- coding: utf-8 -*-
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

print isEnglish('slabiky, ale liší se podle významu')
print isEnglish('English')
print isEnglish('ގެ ފުރަތަމަ ދެ އަކުރު ކަ')
print isEnglish('how about this one : 通 asfަ')
print isEnglish('?fd4))45s&')

#It will return F, T, F, F, T

	