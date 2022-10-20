

DROP TABLE IF EXISTS ;
CREATE TABLE  (
  CURENTSTID integer NOT NULL,
  NAME text NOT NULL
);

COMMENT ON COLUMN .CURENTSTID IS 'Идентификатор статуса (ключ)';
COMMENT ON COLUMN .NAME IS 'Наименование (0 - актуальный, 1-50, 2-98 – исторический (кроме 51), 51 - переподчиненный, 99 - несуществующий)';
