CREATE TYPE account_type AS ENUM ('checking', 'savings', 'cd', 'money_market');

CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY,
    account_type account_type,
    balance INTEGER
);
-- Do not modify above this line --


INSERT INTO bank_accounts (id, balance, account_type)
  VALUES (1, 1000, 'checking'),
    (2, 2000, 'savings'),
    (3, 3000, 'cd'),
    (4, 4000, 'money_market');







-- Do not modify below this line --
SELECT * FROM bank_accounts;
