
 
DROP TABLE IF EXISTS ;
CREATE TABLE  (
  NDTYPEID integer NOT NULL,
  NAME text NOT NULL
);
 
COMMENT ON COLUMN .NDTYPEID IS 'Идентификатор записи (ключ)';
COMMENT ON COLUMN .NAME IS 'Наименование типа нормативного документа';