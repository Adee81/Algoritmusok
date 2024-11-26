# Jack goes to Rapture megoldása

## Megoldás lépései

1. **Gráf felépítése:**

   - Először létrehozunk egy gráf struktúrát, ahol minden csúcs tárolja a hozzá kapcsolódó éleket és ezek súlyait. Ez segít abban, hogy könnyen hozzáférjünk az összekapcsolt állomásokhoz és azok viteldíjaihoz.

2. **Dijkstra algoritmus használata:** 

   - A Dijkstra algoritmus egy hatékony módszer a legkisebb költségű útvonal megtalálására súlyozott gráfokban. Egy prioritási sort használunk (min-heap), amelyben az állomásokat a hozzájuk tartozó aktuális minimális költséggel tároljuk.
   - Inicializáljuk az algoritmust az első csúccsal, ahol a kezdeti költséget 0-nak állítjuk be.

3. **Ciklus az élek bejárásához:** 

   - Amíg a prioritási sor nem üres, folyamatosan kivesszük a legkisebb költségű csúcsot, és frissítjük a szomszédos csúcsokhoz tartozó minimális költségeket.
   - Minden egyes állomás esetében kiszámoljuk az új költséget úgy, hogy figyelembe vesszük a különbséget az aktuális és a szomszédos állomás költségei között.

4. **Eredmény meghatározása:** 

   - A ciklus végén megnézzük az utolsó csúcs minimális költségét. Ha ez a költség továbbra is végtelen (ami azt jelenti, hogy nincs elérhető útvonal az utolsó állomásig), akkor kiírjuk, hogy "NO PATH EXISTS". Ellenkező esetben kiírjuk a megtalált legkisebb költséget.