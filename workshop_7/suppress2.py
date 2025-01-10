
def suppress2(vals):
    if isinstance(vals, (str, dict, tuple)):
        print("Error: input must be a list")
        return None

    r=[]
    for x in vals:
        if isinstance(vals, (str, dict, tuple)):
            print("Not a number")
            return None
        elif x<5:
            r.append(0)
        else:
            r.append(round(x/5)*5)
    return r
