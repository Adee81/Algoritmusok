# Kommandó

Link: https://www.spoj.com/problems/APIO10A/

Te vagy a parancsnok egy n katonából álló csapatban, akik 1-től n-ig vannak számozva. A közelgő csatára ezekből a katonákból több kommandós egységet tervezel kialakítani. Az egység előmozdítása és a morál növelése érdekében minden egység egy összefüggő katonai sorozatból áll majd, azaz (i, i+1 ... i+k) formában.

Minden katona i harci hatékonysága x<sub>i</sub>. Eredetileg egy kommandós egység (i, i+1, ..., i+k) harci hatékonyságát az egység tagjainak egyéni harci hatékonyságának összegeként számították ki. Más szóval:
x = x<sub>i</sub> + x<sub>i+1</sub> + ··· + x<sub>i+k</sub>.

Azonban az évek során elért dicsőséges győzelmek alapján arra a következtetésre jutottál, hogy az egység harci hatékonyságát az alábbi módon kell módosítani:

Az új hatékonyság x a következő egyenlet alapján kerül kiszámításra:
x = ax<sup>2</sup> + bx + c, ahol a, b, c ismert együtthatók (a < 0), x pedig az egység eredeti hatékonysága.

A feladatod parancsnokként az, hogy a katonáidat olyan kommandós egységekre oszd fel, amelyek összesített módosított hatékonysága a lehető legnagyobb.

Például tegyük fel, hogy van 4 katonád, x<sub>1</sub> = 2, x<sub>2</sub> = 2, x<sub>3</sub> = 3, x<sub>4</sub> = 4. Továbbá, az egység harci hatékonyságának módosításához szükséges együtthatók a következők: a = −1, b = 10, c = −20. Ebben az esetben a legjobb megoldás az, hogy a katonákat három kommandó egységre osztod: Az első egység tartalmazza az 1-es és 2-es katonát, a második egység a 3-as katonát, a harmadik egység pedig a 4-es katonát. Az egységek harci hatékonysága rendre 4, 3, 4, és a módosított hatékonyságok rendre 4, 1, 4. Az összesített módosított hatékonyság ebben a csoportosításban 9, és ellenőrizhető, hogy ennél jobb megoldás nem lehetséges.

### Input

- Első sor: <b>T, az esetek száma</b>.
- Minden eset három sorból áll.
- Az első sor egy pozitív egész számot tartalmaz n, a katonák teljes számát.
- A második sor három egész számot tartalmaz: a, b és c, szóközzel elválasztva, az egység harci hatékonyságának módosításához szükséges együtthatók.
- Az utolsó sor n egész számot tartalmaz x<sub>1</sub>, x<sub>2</sub> ... x<sub>n</sub>, szóközzel elválasztva, amelyek a katonák 1, 2 ... n harci hatékonyságát jelölik.

### Korlátozások

T ≤ 3

n ≤ 1, 000, 000

−5 ≤ a ≤ −1

|b| ≤ 10, 000, 000

|c| ≤ 10, 000, 000

1 ≤ xi ≤ 100

### Kimenet

Minden válasz egy külön sorban jelenjen meg.

### Minta

#### Bemenet:

3  
4  
-1 10 -20  
2 2 3 4  
5  
-1 10 -20  
1 2 3 4 5  
8  
-2 4 3  
100 12 3 4 5 2 4 2  

#### Kimenet:

9  
13  
-19884
