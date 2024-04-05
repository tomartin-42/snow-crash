### LEVEL14 (BONUS)

- There are no files.

- The only binary we can use is `getflag`.

- We use gdb.
    ```bash
    gdb getflag
    r
    Starting program: /bin/getflag
    You should not reverse this
    [Inferior 1 (process 1998) exited with code 01]
    ```

- It detects that we are in debug mode and kicks us out.

- First, we need to bypass this protection.

- The `ptrace` function is the one checking if we are in debugging.

- It's returning -1, we need to change the value to `>= 0`.
    ```bash
   gdb /bin/getflag
   b main
   r
   b *0x0804898e ->    0x0804898e <+72>:	test   %eax,%eax
   c
   p $eax 
   $1 = -1
   p $eax = 0
   $2 = 0
   ```

- Now we need to change the UID to 3014, which is the UID that obtains the flag.
    ```bash
    b getuid
    c
    n
    p $eax 
    $3 = 2014
    p $eax = 3014
    p $eax
    $4 = 3014
    c
    Continuing.
    Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
    [Inferior 1 (process 2161) exited normally]
    ```

- Done!!!

---

### LEVEL14 (BONUS)

- No hay ningún archivo

- El uníco binario que podemos usar es el `getflag`

- Usamos gdb
    ```bash
    gdb getflag
    r
    Starting program: /bin/getflag
    You should not reverse this
    [Inferior 1 (process 1998) exited with code 01]
    ```

- Detecta que estamo en debug y nos echa

- Primero hay que saltarse esta protección

- la funcion `ptrace` es la que comprueba si estamos en debugging

- Está devolviendo -1, hay que canviar el valor a `>= 0`
    ```bash
   gdb /bin/getflag
   b main
   r
   b *0x0804898e ->    0x0804898e <+72>:	test   %eax,%eax
   c
   p $eax 
   $1 = -1
   p $eax = 0
   $2 = 0
   ```

- Ahora hay que cambiar el UID a 3014 que es el UID que obtinen la flag
    ```bash
    b getuid
    c
    n
    p $eax 
    $3 = 2014
    p $eax = 3014
    p $eax
    $4 = 3014
    c
    Continuing.
    Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
    [Inferior 1 (process 2161) exited normally]
    ```


