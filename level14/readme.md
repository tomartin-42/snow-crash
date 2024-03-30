- No hay ningún archivo
- El uníco binario que podemso usar es el getflag
- Usamos gdb
    gdb getflag
    r
    Starting program: /bin/getflag
    You should not reverse this
    [Inferior 1 (process 1998) exited with code 01]
- Detecta que estamo en debug y nos echa
- Primero hay que saltarse esta protección
   la funcion ptrace es la que comprueba si estamos en debugging
   está devolviendo -1, hay que canviar el valor a 0
   gdb getflag
   b main
   r
   b *0x0804898e ->    0x0804898e <+72>:	test   %eax,%eax
   c
   p $eax -> -1
   p $eax=0
   p $eax -> 0
- Ahora hay que cambiar el UID a 3014 que es el UID que obtinen la flag
    b getuid
    c
    n
    p $eax -> 2014
    p $eax=3014
    p $eax -> 3014
    c
    Done!!!1

