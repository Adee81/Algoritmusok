
# KnightL on a Chessboard - Megoldás

Ez a megoldás a KnightL nevű speciális "lovag" figura lépéseit modellezi egy \(n x n)-es sakktáblán. A cél az, hogy megtaláljuk a minimális lépésszámot, amely szükséges ahhoz, hogy a KnightL egy adott lépéspár (a,b) esetén a (0,0) kezdőpozícióból az (n-1,n-1) végcélba jusson.
A feladatot Python nyelven oldottam meg.

## Áttekintés
A megoldás alapját egy szélességi keresés (BFS - Breadth-First Search) algoritmus képezi, ami tipikusan a legrövidebb út megtalálására szolgál egy gráfban. Ebben az esetben a sakktábla mezői képezik a gráf csúcsait, és a KnightL lépései (az (a,b) és (b,a) mozgások) alkotják az éleket.

## Megoldás Lépései

1. **Eredménytábla inicializálása**: 
    - Egy kétdimenziós listát (`result`) hozunk létre, amely tárolja az egyes (a,b) párok minimális lépésszámát. Ez a tábla lesz a végeredmény.
  
2. **BFS alkalmazása** minden egyes (a,b) lépéskombinációra:
    - Az algoritmus minden (a,b) pár esetén elindít egy keresést a (0,0) pozícióból.
    - Egy várólistát (`queue`) használunk a következő pozíciók nyomon követésére, amit a BFS algoritmus során dolgozunk fel. A `queue` elemei tartalmazzák az aktuális pozíciót és az eddigi lépések számát.
    - Egy látogatott mezőket (`visited`) tartalmazó kétdimenziós listát hozunk létre annak biztosítására, hogy minden mezőt csak egyszer látogassunk meg.

3. **Lépések végrehajtása**:
    - A keresés során minden lehetséges lépést megvizsgálunk az aktuális pozícióból.
    - Az algoritmus nyolc lehetséges új pozíciót generál az (a,b) és (b,a) lépések alapján (pozitív és negatív irányokban is).
    - Csak azokat a pozíciókat vesszük figyelembe, amelyek még a sakktábla belsejében vannak és amelyeket még nem látogattunk meg.
    - Ha a célmezőt (n-1, n-1) sikeresen elérjük, akkor az eredménytábla megfelelő mezőjét az aktuális lépésszámmal frissítjük.

4. **Lépések számának eltárolása**:
    - Ha egy adott (a,b) párral nem sikerül elérni az (n-1, n-1) célpontot, akkor az adott eredménytábla mezőjét -1 értékkel töltjük ki.

5. **Kimenet létrehozása**:
    - Az algoritmus a megfelelő formátumban írja ki az eredménytáblát, amely n-1 sort és n-1 oszlopot tartalmaz.
