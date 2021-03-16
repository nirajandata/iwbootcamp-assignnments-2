def cam_cases(text,sep):
    res = [text[0].lower()]
    for c in text[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append(sep)
            res.append(c.lower())
        else:
            res.append(c)
     
    return ''.join(res)
     
print(cam_cases("MyNameIs","-"))