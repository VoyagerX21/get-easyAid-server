from app.data.sysprompts import first, second
from app.utils.personalization import personalisedDetails

def promptGen(data, flag):
    r = personalisedDetails(data)
    if flag == 1:
        p1 = r+first
        return p1
    else:
        p2 = r+second
        return p2