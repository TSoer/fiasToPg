

DROP TABLE IF EXISTS ;
CREATE TABLE  (
  POSTALCODE text,
  REGIONCODE text,
  IFNSFL text,
  TERRIFNSFL text,
  IFNSUL text,
  TERRIFNSUL text,
  OKATO text,
  OKTMO text,
  UPDATEDATE date NOT NULL,
  HOUSENUM text,
  ESTSTATUS integer NOT NULL,
  BUILDNUM text,
  STRUCNUM text,
  STRSTATUS integer,
  HOUSEID text NOT NULL,
  HOUSEGUID text NOT NULL,
  AOGUID text NOT NULL,
  STARTDATE date NOT NULL,
  ENDDATE date NOT NULL,
  STATSTATUS integer NOT NULL,
  NORMDOC text,
  COUNTER integer NOT NULL,
  CADNUM text,
  DIVTYPE  NOT NULL
);

COMMENT ON COLUMN .POSTALCODE IS 'Почтовый индекс';
COMMENT ON COLUMN .REGIONCODE IS 'Код региона';
COMMENT ON COLUMN .IFNSFL IS 'Код ИФНС ФЛ';
COMMENT ON COLUMN .TERRIFNSFL IS 'Код территориального участка ИФНС ФЛ';
COMMENT ON COLUMN .IFNSUL IS 'Код ИФНС ЮЛ';
COMMENT ON COLUMN .TERRIFNSUL IS 'Код территориального участка ИФНС ЮЛ';
COMMENT ON COLUMN .OKATO IS 'OKATO';
COMMENT ON COLUMN .OKTMO IS 'OKTMO';
COMMENT ON COLUMN .UPDATEDATE IS 'Дата время внесения записи';
COMMENT ON COLUMN .HOUSENUM IS 'Номер дома';
COMMENT ON COLUMN .ESTSTATUS IS 'Признак владения';
COMMENT ON COLUMN .BUILDNUM IS 'Номер корпуса';
COMMENT ON COLUMN .STRUCNUM IS 'Номер строения';
COMMENT ON COLUMN .STRSTATUS IS 'Признак строения';
COMMENT ON COLUMN .HOUSEID IS 'Уникальный идентификатор записи дома';
COMMENT ON COLUMN .HOUSEGUID IS 'Глобальный уникальный идентификатор дома';
COMMENT ON COLUMN .AOGUID IS 'Guid записи родительского объекта (улицы, города, населенного пункта и т.п.)';
COMMENT ON COLUMN .STARTDATE IS 'Начало действия записи';
COMMENT ON COLUMN .ENDDATE IS 'Окончание действия записи';
COMMENT ON COLUMN .STATSTATUS IS 'Состояние дома';
COMMENT ON COLUMN .NORMDOC IS 'Внешний ключ на нормативный документ';
COMMENT ON COLUMN .COUNTER IS 'Счетчик записей домов для КЛАДР 4';
COMMENT ON COLUMN .CADNUM IS 'Кадастровый номер';
COMMENT ON COLUMN .DIVTYPE IS 'Тип адресации:';
