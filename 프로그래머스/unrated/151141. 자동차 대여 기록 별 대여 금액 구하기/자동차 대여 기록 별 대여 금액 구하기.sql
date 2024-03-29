-- 코드를 입력하세요
SELECT 
DISTINCT C.HISTORY_ID,
CASE
    WHEN (DATEDIFF(C.END_DATE,C.START_DATE)+1) BETWEEN 7 AND 29 THEN FLOOR(C.DAILY_FEE*(DATEDIFF(C.END_DATE,C.START_DATE)+1)*0.95)
    WHEN (DATEDIFF(C.END_DATE,C.START_DATE)+1) BETWEEN 30 AND 89 THEN FLOOR(C.DAILY_FEE*(DATEDIFF(C.END_DATE,C.START_DATE)+1)*0.92)
    WHEN (DATEDIFF(C.END_DATE,C.START_DATE)+1) >= 90 THEN FLOOR(C.DAILY_FEE*(DATEDIFF(C.END_DATE,C.START_DATE)+1)*0.85) 
    ELSE ROUND(C.DAILY_FEE*(DATEDIFF(C.END_DATE,C.START_DATE)+1))
END AS FEE
FROM (SELECT A.CAR_ID, A.CAR_TYPE, A.DAILY_FEE, A.OPTIONS,
      B.HISTORY_ID, B.START_DATE, B.END_DATE
      FROM CAR_RENTAL_COMPANY_CAR A
      INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B
      ON A.CAR_ID=B.CAR_ID) AS C
INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
ON C.CAR_TYPE=D.CAR_TYPE
WHERE C.CAR_TYPE='트럭'
ORDER BY 2 DESC,1 DESC;