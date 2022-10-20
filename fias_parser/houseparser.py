from pgsqlconnector import pgsqlConnection
from xml.etree.cElementTree import iterparse


def parseHouses(file, region):
    conn = pgsqlConnection()
    cur = conn.cursor()

    print(conn)

    context = iter(iterparse(open(file, encoding='utf_8_sig'),
                             events=('start', 'end')))

    _, root = next(context)

    for event, elem in context:
        if event == 'end' and elem.tag == 'House':

            attrib = elem.attrib

            REGIONCODE = attrib.get("REGIONCODE", '')

            if REGIONCODE == region:
                cur.execute(
                    """ INSERT INTO hous ("AOGUID", "BUILDNUM", "ENDDATE", "ESTSTATUS", "HOUSEGUID", "HOUSEID", "HOUSENUM", "POSTALCODE", "STARTDATE", "STRUCNUM", "UPDATEDATE", "COUNTER", "REGIONCODE", "STRSTATUS") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (
                        attrib.get("AOGUID", ''),
                        attrib.get("BUILDNUM", ''),
                        attrib.get("ENDDATE", ''),
                        attrib.get("ESTSTATUS", 0),
                        attrib.get("HOUSEGUID", ''),
                        attrib.get("HOUSEID", ''),
                        attrib.get("HOUSENUM", ''),
                        attrib.get("POSTALCODE", 0),
                        attrib["STARTDATE"],
                        attrib.get("STRUCNUM", ''),
                        attrib["UPDATEDATE"],
                        attrib.get("COUNTER", 0),
                        attrib.get("REGIONCODE", 0),
                        attrib.get("STRSTATUS", 0)
                    )
                )

                conn.commit()

        root.clear()

    cur.close()
    conn.close()
