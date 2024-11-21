# Construct the Array

link: https://www.hackerrank.com/challenges/construct-the-array/problem?isFullScreen=false

A cél az, hogy találjunk olyan módszereket, amelyekkel létrehozhatunk egy tömböt úgy, hogy az egymást követő pozíciókban lévő értékek különbözőek legyenek.

## Feladat leírása

Konkrétan, olyan tömböt szeretnénk létrehozni, amelynek \( n \) eleme van, ahol minden elem értéke \( 1 \) és \( k \) között van (mindkettő beleértendő). Továbbá azt akarjuk, hogy a tömb első eleme fixen 1 és az utolsó eleme \( x \) legyen.

Adott \( n \), \( k \) és \( x \). Azt kell megtalálnunk, hogy hányféleképpen lehet létrehozni ilyen tömböt. Mivel a válasz nagy lehet, az eredményt modulo \( 10^9+7 \)-tel kell megadni.

## Példa

Ha \( n = 4 \), \( k = 3 \), \( x = 2 \), akkor **3 mód** létezik, ahogy az alábbiakban látható.


![Mintakep](https://s3.amazonaws.com/hr-assets/0/1511427084-cd3fbbf0e1-FILLARRAY.png)

## Feladat

Írjuk meg a countArray függvényt, amely bemenetként megkapja \( n \)-t, \( k \)-t és \( x \)-et, majd vissztér a lehetséges módok számával, amelyekkel létrehozható a tömb úgy, hogy az egymást követő elemek eltérjenek egymástól.

## Korlátozások

- <sub>3 ≤ n ≤ 10^5</sub>
- <sub>2 ≤ n ≤ 10^55</sub> 
- <sub>1 ≤ x ≤ k</sub> 

## Mintabemenet

```plaintext
n = 4, k = 3, x = 2
```

## Mintakimenet

```plaintext
3
```