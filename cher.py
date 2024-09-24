
def prov_time(time):
    pr = True
    try:
        a = time.split(':')
        h = int(a[0])
        m = int(a[1])
        if h < 0 or h > 24:
            pr = False
        if m < 0 or m > 60:
            pr = False
    except:
        pr = False
    return pr
print(prov_time('23:54'))