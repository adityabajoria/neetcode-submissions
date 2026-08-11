CREATE TABLE stocks (
  id INTEGER PRIMARY KEY,
  name TEXT,
  transaction_dates DATE[]
);

-- Do not modify above this line --
INSERT INTO stocks (transaction_dates, name, id)
VALUES
    (ARRAY['2007-02-09', '2007-02-10', '2007-02-11']::DATE[], 'AAPL', 1),
    (ARRAY['2004-12-15', '2004-12-16']::DATE[], 'GOOG', 2);



-- Do not modify below this line --
SELECT * FROM stocks;
