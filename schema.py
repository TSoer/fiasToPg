schema = [
  {
    "tablename": "actstat",
    "fields": [
      {
        "name": "ACTSTATID",
        "type": "smallint",
        "restrictions": ["not null"],
        "pkey": True
      },
      {
        "name": "NAME",
        "type": "character varying(100)",
        "restrictions": ["not null"]
      }
    ]
  },
  {
    "tablename": "addrobj",
    "fields": [
      {
        "name": "AOGUID",
        "type": "character varying(36)",
        "restrictions": ["not null"]
      },
      {
        "name": "FORMALNAME",
        "type": "character varying(120)",
        "restrictions": ["not null"]
      },
      {
        "name": "REGIONCODE",
        "type": "character varying(2)",
        "restrictions": ["not null"]
      },
      {
        "name": "AUTOCODE",
        "type": "character varying(1)",
        "restrictions": ["not null"]
      },
      {
        "name": "AREACODE",
        "type": "character varying(3)",
        "restrictions": ["not null"]
      },
      {
        "name": "CITYCODE",
        "type": "character varying(3)",
        "restrictions": ["not null"]
      },
      {
        "name": "CTARCODE",
        "type": "character varying(3)",
        "restrictions": ["not null"]
      },
      {
        "name": "PLACECODE",
        "type": "character varying(3)",
        "restrictions": ["not null"]
      },
      {
        "name": "PLANCODE",
        "type": "character varying(4)",
        "restrictions": ["not null"]
      },
      {
        "name": "STREETCODE",
        "type": "character varying(4)",
        "restrictions": ["not null"]
      },
      {
        "name": "EXTRCODE",
        "type": "character varying(4)",
        "restrictions": ["not null"]
      },
      {
        "name": "SEXTCODE",
        "type": "character varying(3)",
        "restrictions": ["not null"]
      },
      {
        "name": "OFFNAME",
        "type": "character varying(120)",
        "restrictions": []
      },
      {
        "name": "POSTALCODE",
        "type": "character varying(6)",
        "restrictions": []
      },
      {
        "name": "IFNSFL",
        "type": "character varying(4)",
        "restrictions": []
      },
      {
        "name": "TERRIFNSFL",
        "type": "character varying(4)",
        "restrictions": []
      },
      {
        "name": "IFNSUL",
        "type": "character varying(4)",
        "restrictions": []
      },
      {
        "name": "TERRIFNSUL",
        "type": "character varying(4)",
        "restrictions": []
      },
      {
        "name": "OKATO",
        "type": "character varying(11)",
        "restrictions": []
      },
      {
        "name": "OKTMO",
        "type": "character varying(11)",
        "restrictions": []
      },
      {
        "name": "UPDATEDATE",
        "type": "date",
        "restrictions": ["not null"]
      },
      {
        "name": "SHORTNAME",
        "type": "character varying(10)",
        "restrictions": ["not null"]
      },
      {
        "name": "AOLEVEL",
        "type": "integer",
        "restrictions": ["not null"]
      },
      {
        "name": "PARENTGUID",
        "type": "character varying(36)",
        "restrictions": []
      },
      {
        "name": "AOID",
        "type": "character varying(36)",
        "restrictions": ["not null"],
        "pkey": True
      },
      {
        "name": "PREVID",
        "type": "character varying(36)",
        "restrictions": []
      },
      {
        "name": "NEXTID",
        "type": "character varying(36)",
        "restrictions": []
      },
      {
        "name": "CODE",
        "type": "character varying(17)",
        "restrictions": []
      },
      {
        "name": "PLAINCODE",
        "type": "character varying(15)",
        "restrictions": []
      },
      {
        "name": "ACTSTATUS",
        "type": "integer",
        "restrictions": ["not null"]
      },
      {
        "name": "CENTSTATUS",
        "type": "integer",
        "restrictions": ["not null"]
      },
      {
        "name": "OPERSTATUS",
        "type": "integer",
        "restrictions": ["not null"]
      },
      {
        "name": "CURRSTATUS",
        "type": "integer",
        "restrictions": []
      },
      {
        "name": "STARTDATE",
        "type": "date",
        "restrictions": ["not null"]
      },
      {
        "name": "ENDDATE",
        "type": "date",
        "restrictions": ["not null"]
      },
      {
        "name": "NORMDOC",
        "type": "character varying(36)",
        "restrictions": []
      },
      {
        "name": "LIVESTATUS",
        "type": "boolean",
        "restrictions": ["not null"]
      },
      {
        "name": "DIVTYPE",
        "type": "smallint",
        "restrictions": ["not null"]
      }
    ]
  },
  {
    "tablename": "centerst",
    "fields": [
      {
        "name": "CENTERSTID",
        "type": "smallint",
        "restrictions": ["not null"],
        "pkey": True
      },
      {
        "name": "NAME",
        "type": "character varying(100)",
        "restrictions": ["not null"]
      }
    ]
  },
  {
    "tablename": "currentst",
    "fields": [
      {
        "name": "CURRENTSTID",
        "type": "smallint",
        "restrictions": ["not null"],
        "pkey": True
      },
      {
        "name": "NAME",
        "type": "character varying(100)",
        "restrictions": ["not null"]
      }
    ]
  },
  {
    "tablename": "eststat",
    "fields": [
      {
        "name": "ESTSTATID",
        "type": "smallint",
        "restrictions": ["not null"],
        "pkey": True
      },
      {
        "name": "NAME",
        "type": "character varying(20)",
        "restrictions": ["not null"]
      },
      {
        "name": "SHORTNAME",
        "type": "character varying(20)",
        "restrictions": ["not null"]
      }
    ]
  },
  {
    "tablename": "flattype",
    "fields": [
      {
        "name": "FLTYPEID",
        "type": "smallint",
        "restrictions": ["not null"],
        "pkey": True
      },
      {
        "name": "NAME",
        "type": "character varying(20)",
        "restrictions": ["not null"]
      },
      {
        "name": "SHORTNAME",
        "type": "character varying(20)",
        "restrictions": ["not null"]
      }
    ]
  },
  {
    "tablename": "house",
    "fields": [
      {
        "name": "AOGUID",
        "type": "character varying(36)",
        "restrictions": ["not null"]
      },
      {
        "name": "REGIONCODE",
        "type": "character varying(2)",
        "restrictions": ["not null"]
      },
      {
        "name": "POSTALCODE",
        "type": "character varying(6)",
        "restrictions": []
      },
      {
        "name": "IFNSFL",
        "type": "character varying(4)",
        "restrictions": []
      },
      {
        "name": "TERRIFNSFL",
        "type": "character varying(4)",
        "restrictions": []
      },
      {
        "name": "IFNSUL",
        "type": "character varying(4)",
        "restrictions": []
      },
      {
        "name": "TERRIFNSUL",
        "type": "character varying(4)",
        "restrictions": []
      },
      {
        "name": "OKATO",
        "type": "character varying(11)",
        "restrictions": []
      },
      {
        "name": "OKTMO",
        "type": "character varying(11)",
        "restrictions": []
      },
      {
        "name": "UPDATEDATE",
        "type": "date",
        "restrictions": ["not null"]
      },
      {
        "name": "HOUSENUM",
        "type": "character varying(20)",
        "restrictions": []
      },
      {
        "name": "HOUSEGUID",
        "type": "character varying(36)",
        "restrictions": []
      },
      {
        "name": "HOUSEID",
        "type": "character varying(36)",
        "restrictions": ["not null"],
        "pkey": True
      },
      {
        "name": "CADNUM",
        "type": "character varying(100)",
        "restrictions": []
      },
      {
        "name": "COUNTER",
        "type": "integer",
        "restrictions": ["not null"]
      },
      {
        "name": "STATSTATUS",
        "type": "integer",
        "restrictions": ["not null"]
      },
      {
        "name": "STRSTATUS",
        "type": "integer",
        "restrictions": []
      },
      {
        "name": "BUILDNUM",
        "type": "character varying(50)",
        "restrictions": []
      },
      {
        "name": "ESTSTATUS",
        "type": "integer",
        "restrictions": ["not null"]
      },
      {
        "name": "STARTDATE",
        "type": "date",
        "restrictions": ["not null"]
      },
      {
        "name": "ENDDATE",
        "type": "date",
        "restrictions": ["not null"]
      },
      {
        "name": "NORMDOC",
        "type": "character varying(36)",
        "restrictions": []
      },
      {
        "name": "STRUCNUM",
        "type": "character varying(50)",
        "restrictions": []
      },
      {
        "name": "DIVTYPE",
        "type": "smallint",
        "restrictions": ["not null"]
      }
    ]
  },
  {
    "tablename": "ndoctype",
    "fields": [
      {
        "name": "NDTYPEIDID",
        "type": "integer",
        "restrictions": ["not null"],
        "pkey": True
      },
      {
        "name": "NAME",
        "type": "character varying(250)",
        "restrictions": ["not null"]
      }
    ]
  },
]