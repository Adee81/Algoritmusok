# 4. Fák, Gráfok
## KnightL on a Chessboard

Link: https://www.hackerrank.com/challenges/knightl-on-chessboard/problem?isFullScreen=false

KnightL egy sakkfigura a sakktáblán, amely L alakban mozog.  Meghatározzuk a KnightL(a, b) lehetséges lépéseit egy (x<sub>1</sub>, y<sub>1</sub>) pozícióból egy (x<sub>2</sub>, y<sub>2</sub>) pozícióba, amely megfelel az alábbi feltételek valamelyikének:
<ul>
    <li>
        x<sub>2</sub> = x<sub>1</sub>± a és y<sub>2</sub> = y<sub>1</sub>± b vagy
    </li>
    <li>
        x<sub>2</sub> = x<sub>1</sub>± b és y<sub>2</sub> = y<sub>1</sub>± a
    </li>
</ul>
<p>Megjegyezzük, hogy (a,b) és (b,a) ugyanazokat a mozgási lehetőségeket kínálja.
Egy n x n-es sakktábla esetén, ahol az n értéke adott, válaszoljuk meg a következő kérdést minden (a,b) párra, ahol 1 ≤ a,b < n:
<li>Mi a minimális lépésszám, amely szükséges ahhoz, hogy a KnightL(a,b) a (0,0) pozícióból az (n-1,n-1) pozícióba jusson? (0,0) = sakktábla bal felső sarka, (n-1,n-1) = sakktábla jobb alsó sarka</li></p>
<p>Mivel 1 ≤ a,b < n, ebből kifolyólag KnightL nem csak a szokásos L alakú ((a=1, b= 2) vagy (a=2, b=1)) lépéseket tudja felvenni, ami megfelelne a hagyományos sakk szabályainak, hanem a és b értéke külön-külön is felveszi az értékeket 1-től n-1-ig.</p>

<b>Bemenet:</b>
<p>Egy darab integer (n), ami meghatározza a sakktábla méretét (n x n).</p>

<b>Kimeneti formátum:</b>
<p>Pontosan n-1 sort kell kiírni, ahol minden i sor (ahol 1 ≤ i < n) n-1 szóközzel elválasztott egész számot tartalmaz, amelyek azt írják le, hogy a KnightL(i, j) számára mi a minimális lépésszám a megfelelő j-re (ahol 1 ≤ j < n). Ha KnightL(i,j) nem tudja elérni az (n-1,n-1) pozíciót, akkor a kimenet -1 legyen.</p>
