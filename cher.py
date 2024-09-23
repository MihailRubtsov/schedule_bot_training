def prov_time(mot):
    pr = True

    if len(mot) <= 5 or int(mot[:2]) <0 or int(mot[:2]) > 24 or int(mot[3:]) <0 or int(mot[3:]) > 60:
        pr = False
    return pr



print(prov_time('0^45'))