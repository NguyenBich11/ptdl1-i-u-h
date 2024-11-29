create database dbPythonTestSQL
use dbPythonTestSQL
CREATE TABLE tblUsers (
    uid VARCHAR(5) NOT NULL PRIMARY KEY,
    unname NVARCHAR(25),
    ubirthdate DATE,
    usalary FLOAT,
    urank INT
);
--nạp dữ liệu
INSERT INTO tblUsers (uid, unname, ubirthdate, usalary, urank)
VALUES
    ('u001', N'Henry', '2001-07-31',125.5, 1),
    ('u002', N'Peter', '1980-08-25', 500, 1),
    ('u003', N'Owen', '1995-02-28', 275.5, 2),
    ('u004', N'Jackson', '2002-04-25', 400, 4),
	('u005', N'Ellite', '2000-05-20', 600, 3);
select*from tblUsers
--Lấy người sao cho năm hiện tại-năm ubirthdate=35
SELECT *
FROM tblUsers
WHERE DATEPART(YEAR, GETDATE()) - DATEPART(YEAR, ubirthdate) <=35;