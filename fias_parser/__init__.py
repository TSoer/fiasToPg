from addressparser import parseAddress
from houseparser import parseHouses

REGIONCODE = 30
ADDRSFILEPATH = "AS_ADDROBJ.xml"
HOUSFILEPATH = "AS_HOUSE.xml"

parseAddress(ADDRSFILEPATH, REGIONCODE)
parseHouses(HOUSFILEPATH, REGIONCODE)
