# Construct the Array megoldása

A feladat célja, hogy meghatározzuk, hány különböző tömböt lehet létrehozni a következő feltételek mellett:
1. A tömb hossza \( n \).
2. Az elemek értékei \( 1 \) és \( k \) között legyenek.
3. Az első elem mindig \( 1 \).
4. Az utolsó elem mindig \( x \).
5. Az egymást követő elemek értéke mindig eltérő.

Az eredményt modulo \( 10^9 + 7 \)-tel kell visszaadni.

---

## Megoldás leírása

### Alapötlet
A probléma dinamikus programozással oldható meg, ahol két értéket követünk nyomon:
- **`endx`**: Azoknak a tömböknek a száma, amelyek utolsó eleme \( x \).
- **`end`**: Azoknak a tömböknek a száma, amelyek utolsó eleme **nem \( x \)**.

Minden iterációval kiszámoljuk, hogyan változik ez a két érték, amikor a tömb hossza növekszik.

### Kezdeti állapotok
1. **Ha az utolsó elem \( x \):**
   - `endx = 1`
   - `end = 0`
2. **Ha az utolsó elem nem \( x \):**
   - `endx = 0`
   - `end = 1`

### Iterációs folyamat
Minden iteráció egy új elem hozzáadását modellezi a tömbhöz:
1. **Az új tömb utolsó eleme \( x \):**  
   Ezt csak akkor érhetjük el, ha az előző tömb utolsó eleme **nem \( x \)**. Így: `endx = end`


2. **Az új tömb utolsó eleme nem \( x \):**  
   Ezt kétféleképpen érhetjük el:
   - Ha az előző tömb utolsó eleme \( x \), akkor \( k-1 \) különböző érték közül választhatjuk az új elemet.
   - Ha az előző tömb utolsó eleme nem \( x \), akkor \( k-2 \) különböző érték közül választhatjuk az új elemet.
\[
\text{end} = (\text{endx} \times (k - 1) + \text{end} \times (k - 2)) \mod \text{MOD}
\]



### Végső eredmény
Az \( n \)-elemű tömbök száma, amelyek megfelelnek a feltételeknek, az `endx` értéke lesz a ciklus végén.

---

## Példa

### Bemenet:

```plaintext
n = 4, k = 3, x = 2
```

### Kimenet

```plaintext
3
```