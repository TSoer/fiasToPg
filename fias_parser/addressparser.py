from pgsqlconnector import pgsqlConnection
from xml.etree.cElementTree import iterparse


def parseAddress(file, region):
    conn = pgsqlConnection()
    cur = conn.cursor()

    print(conn)

    context = iter(iterparse(open(file, encoding='utf_8_sig'), events=('start', 'end')))

    _, root = next(context)

    for event, elem in context:
        if event == 'end' and elem.tag == 'Object':

            attrib = elem.attrib

            REGIONCODE = attrib.get("REGIONCODE", 0)

            if REGIONCODE == region:
                cur.execute(
                    """INSERT INTO addresses ("ACTSTATUS", "AOID", "AOGUID", "AOLEVEL", "CENTSTATUS", "CURRSTATUS", 
                    "ENDDATE", "FORMALNAME", "NEXTID", "OPERSTATUS", "PARENTGUID", "PLAINCODE", "POSTALCODE", 
                    "PREVID", "REGIONCODE", "SHORTNAME", "STARTDATE", "UPDATEDATE", "LIVESTATUS") VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (
                        attrib.get("ACTSTATUS", 0),
                        attrib.get("AOID", ''),
                        attrib.get("AOGUID", ''),
                        attrib.get("AOLEVEL", 0),
                        attrib.get("CENTSTATUS", 0),
                        attrib.get("CURRSTATUS", 0),
                        attrib["ENDDATE"],
                        attrib.get("FORMALNAME", 0),
                        attrib.get("NEXTID", ''),
                        attrib.get("OPERSTATUS", 0),
                        attrib.get("PARENTGUID", ''),
                        attrib.get("PLAINCODE", ''),
                        attrib.get("POSTALCODE", 0),
                        attrib.get("PREVID", ''),
                        attrib.get("REGIONCODE", 0),
                        attrib.get("SHORTNAME", 0),
                        attrib["STARTDATE"],
                        attrib["UPDATEDATE"],
                        attrib.get("LIVESTATUS", 0)
                    ))

                conn.commit()

        root.clear()

    cur.close()
    conn.close()
