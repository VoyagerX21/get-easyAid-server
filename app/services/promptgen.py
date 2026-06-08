from app.data.sysprompts import first, second
from app.utils.personalization import personalisedDetails

def promptGen(data):
    p1 = personalisedDetails(data)+first
    p2 = personalisedDetails(data)+second
    return [p1, p2]