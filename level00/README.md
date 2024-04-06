### LEVEL00
- I'm looking for files owned by the user flag00.
    ```bash
    level00@SnowCrash:~$ find / -user flag00 2>/dev/null
    /usr/sbin/john
    /rofs/usr/sbin/john
    level00@SnowCrash:~$ find / -user flag00 2>/dev/null | xargs cat
    cdiiddwpgswtgt
    cdiiddwpgswtgt
    ```
    
- I try the password with its flag00 but it doesn't work.

- I search if it's a Caesar cipher https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar

- I find that it could be `nottoohardhere`

### LEVEL00

- Busco archivos del propietario flag00
    ```bash
    level00@SnowCrash:~$ find / -user flag00 2>/dev/null
    /usr/sbin/john
    /rofs/usr/sbin/john
    level00@SnowCrash:~$ find / -user flag00 2>/dev/null | xargs cat
    cdiiddwpgswtgt
    cdiiddwpgswtgt
    ```

- Pruebo la passwd con su flag00 pero no funciona

- Busco si es un cifrado César https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar

- Encuentro que puede ser `nottoohardhere`

