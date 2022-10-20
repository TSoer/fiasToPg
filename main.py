#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
"""
Created on 20.08.2021


@author: TSoer
"""

import os
from dbfread import DBF, FieldParser, InvalidValue
import pandas as pd
from sqlalchemy import create_engine


class CustomFieldParser(FieldParser):
    """Вместо пустой строки None"""
    def parseC(self, field, data):
        if data.rstrip(b' ') == b'':
            return None
        else:
            return self.decode_text(data.rstrip(b'\0 '))


class Record:
    """Делать записи в orderdick берадть в DBF как recfactory=Record"""
    def __init__(self, items):
        for (name, value) in items:
            setattr(self, name, value)


class ImportDB:

    def __init__(self, user='postgres',
                       host='127.0.0.1',
                       port='5432',
                       password='postgres',
                       dbname='testapz'):
        self.pathDB = os.path.join(os.path.abspath(os.curdir), 'DBF')
        self.param_dic = {"host": host,
                          "database": dbname,
                          "port": port,
                          "user": user,
                          "password": password,
                          "application_name": 'Rent&Sale of land'}

        connect = "postgresql+psycopg2://%s:%s@%s:5432/%s" % (self.param_dic['user'],
                                                              self.param_dic['password'],
                                                              self.param_dic['host'],
                                                              self.param_dic['database'])
        self.conn = create_engine(connect)
        print(self.conn)

    def dbf2pandas(self):
        """
        Примечание если не хочешь проблем с запросами в базу держи в DBF
        ignorecase=True
        lowernames=True
        """
        for dirpath, dirnames, filenames in os.walk(self.pathDB):
            for filename in filenames:
                print(filename)
                dbf = DBF(os.path.join(self.pathDB, filename),
                          load=False,                        # Не держим в памяти после загрузки
                          ignorecase=True,                   # игнорировать регистер кол.
                          lowernames=True,                   # Формировать представление кол в ниж рег.
                          parserclass=CustomFieldParser,     # Парсим пустые строки вместо "" none
                          ignore_missing_memofile=True)      # при возникновение обки и потери данных None
                print(f'Идет импотр {filename}')
                if filename.startswith('ADDROB'):
                    db = pd.DataFrame(iter(dbf))
                    db.to_sql(name='addrobj',
                              con=self.conn,
                              schema='fias',
                              index=False,
                              if_exists='append',
                              chunksize=50)
                # На тот случай если буду необходимы одеса до квартир
                if filename.startswith('HOUSE'):
                    db = pd.DataFrame(dbf)
                    db.to_sql(name='house',
                              con=self.conn,
                              schema='fias',
                              index=False,
                              if_exists='append',
                              chunksize=50)
                print(f"Закончил импорт {filename}")

    def creatTable(self):
        # TODO MetaData
        table1 = """create table addrobj(
                     "actstatus" integer,
                     "aoguid" character varying(36) collate pg_catalog."default",
                     "aoid" character varying(36) collate pg_catalog."default",
                     "aolevel" integer,
                     "areacode" integer,
                     "autocode" integer,
                     "centstatus" integer,
                     "citycode" integer,
                     "code" character varying(20) collate pg_catalog."default",
                     "currstatus" integer,
                     "enddate" timestamp,
                     "formalname" character varying(120) collate pg_catalog."default",
                     "ifnsfl" integer,
                     "ifnsul" integer,
                     "nextid" character varying(36) collate pg_catalog."default",
                     "offname" character varying(120) collate pg_catalog."default",
                     "okato" varchar(11),
                     "oktmo" varchar(11),
                     "operstatus" integer,
                     "parentguid" character varying(36) collate pg_catalog."default",
                     "placecode" integer,
                     "plaincode" character varying(20) collate pg_catalog."default",
                     "postalcode" integer,
                     "previd" character varying(36) collate pg_catalog."default",
                     "regioncode" integer,
                     "shortname" character varying(15) collate pg_catalog."default",
                     "startdate" timestamp,
                     "streetcode" integer,
                     "terrifnsfl" integer,
                     "terrifnsul" integer,
                     "updatedate" timestamp,
                     "ctarcode" integer,
                     "extrcode" integer,
                     "sextcode" integer,
                     "livestatus" integer,
                     "normdoc" character varying(36) collate pg_catalog."default",
                     "plancode" integer,
                     "cadnum" character varying(100) collate pg_catalog."default",
                     "divtype" integer
                 )
                 with (
                     oids = false
                 )
                 tablespace pg_default;
                 comment on column addrs.id is 'уникальный идентификатор записи. ключевое поле';
                 comment on column addrs.objectid is 'глобальный уникальный идентификатор адресного объекта типа integer';
                 comment on column addrs.objectguid is 'глобальный уникальный идентификатор адресного объекта типа uuid';
                 comment on column addrs.changeid is 'id изменившей транзакции';
                 comment on column addrs.name is 'наименование';
                 comment on column addrs.typename is 'краткое наименование типа объекта';
                 comment on column addrs.level is 'уровень адресного объекта';
                 comment on column addrs.opertypeid is 'статус действия над записью – причина появления записи';
                 comment on column addrs.previd is 'идентификатор записи связывания с предыдущей исторической записью';
                 comment on column addrs.nextid is 'идентификатор записи связывания с последующей исторической записью';
                 comment on column addrs.updatedate is 'дата внесения (обновления) записи';
                 comment on column addrs.startdate is 'начало действия записи';
                 comment on column addrs.enddate is 'окончание действия записи';
                 comment on column addrs.isactual is 'статус актуальности адресного объекта фиас';
                 comment on column addrs.isactive is 'признак действующего адресного объекта';"""
        table2 = """create table house
                     (
                         "aoguid" character varying(36) collate pg_catalog."default",
                         "buildnum" character varying(10) collate pg_catalog."default",
                         "enddate" timestamp,
                         "eststatus" integer,
                         "houseguid" character varying(36) collate pg_catalog."default",
                         "houseid" character varying(36) collate pg_catalog."default",
                         "housenum" character varying(15) collate pg_catalog."default",
                         "statstatus" integer,
                         "ifnsfl" integer,
                         "ifnsul" integer,
                         "okato" varchar(11),
                         "oktmo" varchar(11),
                         "postalcode" integer,
                         "startdate" timestamp,
                         "strucnum" varchar(15),
                         "strstatus" integer,
                         "terrifnsfl" integer,
                         "terrifnsul" integer,
                         "updatedate" timestamp,
                         "normdoc" character varying(36) collate pg_catalog."default",
                         "counter" integer,
                         "cadnum" varchar(50),
                         "divtype" integer
                     )
                     with (
                         oids = false
                     )
                     tablespace pg_default"""
        # self.conn.execute(text(table1))
        # self.conn.execute(text(table2))


if __name__ == '__main__':
    imp = ImportDB()
    imp.dbf2pandas()
    # table = imp.creatTable().lower()
    # print(table)
    print('IMPORT FINISH')
