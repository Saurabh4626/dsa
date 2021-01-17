def replace_pi(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]=="p" and s[1]=="i":
        return "3.14"+replace_pi(s[2:])
    return s[0]+replace_pi(s[1:])
print(replace_pi("pipipirrr"))