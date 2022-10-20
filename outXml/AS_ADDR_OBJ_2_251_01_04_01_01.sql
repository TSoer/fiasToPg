

DROP TABLE IF EXISTS ;
CREATE TABLE  (
  ID  NOT NULL,
  OBJECTID  NOT NULL,
  OBJECTGUID text NOT NULL,
  CHANGEID  NOT NULL,
  NAME text NOT NULL,
  TYPENAME text NOT NULL,
  LEVEL text NOT NULL,
  OPERTYPEID integer NOT NULL,
  PREVID ,
  NEXTID ,
  UPDATEDATE date NOT NULL,
  STARTDATE date NOT NULL,
  ENDDATE date NOT NULL,
  ISACTUAL integer NOT NULL,
  ISACTIVE integer NOT NULL
);

COMMENT ON COLUMN .ID IS 'Уникальный идентификатор записи. Ключевое поле';
COMMENT ON COLUMN .OBJECTID IS 'Глобальный уникальный идентификатор адресного объекта типа INTEGER';
COMMENT ON COLUMN .OBJECTGUID IS 'Глобальный уникальный идентификатор адресного объекта типа UUID';
COMMENT ON COLUMN .CHANGEID IS 'ID изменившей транзакции';
COMMENT ON COLUMN .NAME IS 'Наименование';
COMMENT ON COLUMN .TYPENAME IS 'Краткое наименование типа объекта';
COMMENT ON COLUMN .LEVEL IS 'Уровень адресного объекта';
COMMENT ON COLUMN .OPERTYPEID IS 'Статус действия над записью – причина появления записи';
COMMENT ON COLUMN .PREVID IS 'Идентификатор записи связывания с предыдущей исторической записью';
COMMENT ON COLUMN .NEXTID IS 'Идентификатор записи связывания с последующей исторической записью';
COMMENT ON COLUMN .UPDATEDATE IS 'Дата внесения (обновления) записи';
COMMENT ON COLUMN .STARTDATE IS 'Начало действия записи';
COMMENT ON COLUMN .ENDDATE IS 'Окончание действия записи';
COMMENT ON COLUMN .ISACTUAL IS 'Статус актуальности адресного объекта ФИАС';
COMMENT ON COLUMN .ISACTIVE IS 'Признак действующего адресного объекта';
