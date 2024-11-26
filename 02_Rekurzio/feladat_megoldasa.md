# Bowling Bábuk - Megoldás Működése

Ez a megoldás a **Grundy-számok** elvét alkalmazza, hogy meghatározza, hogy egy adott konfigurációban nyerhető-e a játék, ha mindkét játékos optimálisan játszik. A megoldás **rekurzív** és **memoizált** megközelítést használ, hogy hatékonyan számolja ki a nyerő és vesztes pozíciókat.

## 1. Grundy-számok számítása

A Grundy-számok a **Nim-játék** elve alapján kerülnek kiszámításra. A `f(n)` függvény kiszámítja a Grundy-számot egy `n` hosszúságú bábusorra. A Grundy-számok meghatározása a következő lépésekből áll:

1. **Alapeset**: 
   - Ha nincs bábu, akkor a Grundy-szám 0.
   - Ha egy bábu van, akkor a Grundy-szám 1.
   - Ha két bábu van, akkor a Grundy-szám 2.

2. **Rekurzív lépések**:
   - A `f(n)` függvény rekurzívan kiszámítja a Grundy-számot úgy, hogy minden lehetséges lépést (pl. egy vagy két bábu ledöntése) figyelembe vesz.
   - Minden lépés eredményeként egy új állapot jön létre, amelyet a Grundy-számok `mex` (minimum excludáns) értéke alapján értékelünk.
   - A `mex` az a legkisebb nem-negatív egész szám, amely nem szerepel az elérhető állapotok Grundy-számaiban.

3. **Memoizáció**:
   - Az eredményeket a `g` szótárban tároljuk, hogy elkerüljük az ismétlődő számításokat, és gyorsítsuk a futást.

## 2. Játék kiértékelése

A `isWinning(n, config)` függvény a bemeneti konfiguráció alapján határozza meg, hogy nyerhetünk-e vagy veszítünk:

1. **Szegmensek feldolgozása**:
   - A konfigurációt (`config`) az `'X'` karakterek mentén szétválasztjuk, így egy listát kapunk az álló bábuk szegmenseiről.
   - Például: `IXXIIXIII` → `["I", "", "II", "III"]`.

2. **Grundy-számok számítása**:
   - Minden egyes szegmenshez meghívjuk a `f(c)` függvényt, ahol `c` a szegmens hossza.
   - A Grundy-számokat XOR-ral kombináljuk az összes szegmenshez.

3. **Eredmény meghatározása**:
   - Ha az összegzett XOR értéke **0**, akkor az aktuális pozíció vesztes helyzetet jelent (LOSE).
   - Ha az összegzett XOR értéke **nem 0**, akkor a pozíció nyerő helyzetet jelent (WIN).

## 3. Kód működése

1. **Grundy-számok előállítása**:
   - A `f(n)` függvény kiszámítja az összes lehetséges Grundy-számot rekurzív módon.
   - A memoizációval tárolt értékek gyorsítják a futást, mivel ugyanazokat az állapotokat nem számítjuk újra.

2. **Szegmensek kiértékelése**:
   - A bemeneti konfigurációban az `'I'` és `'X' karakterek` segítségével az álló bábukat külön szegmensekre bontjuk.
   - Az egyes szegmensekhez tartozó Grundy-számok XOR-olása meghatározza az eredményt.

3. **Nyertes vagy vesztes pozíciók**:
   - Az összegzett Grundy-szám alapján meghatározzuk, hogy a játékos **nyer** vagy **veszít**.
