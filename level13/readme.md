### LEVEL13 (BONUS)

- We have a binary.
    ```bash
    level13@SnowCrash:~$ file level13
    level13: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xde91cfbf70ca6632d7e4122f8210985dea778605, not stripped
    ```

- We execute and have this output:
    ```bash
    level13@SnowCrash:~$ ./level13
    UID 2013 started us but we we expect 4242
    ```

- It seems if we manage to have UID 4242, it will give us the token.

- Let's take a look inside the code with Ghidra.
    ```c
    void main(void)

    {
      __uid_t _Var1;
      undefined4 uVar2;
      
      _Var1 = getuid();
      if (_Var1 != 0x1092) {
        _Var1 = getuid();
        printf("UID %d started us but we we expect %d\n",_Var1,0x1092);
                        /* WARNING: Subroutine does not return */
        exit(1);
      }
      uVar2 = ft_des("boe]!ai0FB@.:|L6l@A?>qJ}I");
      printf("your token is %s\n",uVar2);
      return;
    }
    ```

- We see that indeed if we have 4242 as the UID, it will give us the token.

- Let's go to `gdb`:
    ```bash
    gdb level13
    b main
    r
    disassemble
    [...]
    0x0804859a <+14>:	cmp    $0x1092,%eax
    [...]
    b *0x0804859a
    c
    p $eax=0x1092
    c
    your token is 2A31L79asukciNyi8uppkEuSx
    [Inferior 1 (process 2247) exited with code 050]

- We have it!!

---

### LEVEL13 (BONUS)

- Tenemos un binario
    ```bash
    level13@SnowCrash:~$ file level13
    level13: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xde91cfbf70ca6632d7e4122f8210985dea778605, not stripped
    ```

- Ejecutamos y tenemos este output:
    ```bash
    level13@SnowCrash:~$ ./level13
    UID 2013 started us but we we expect 4242
    ```

- Al parece si conseguimos tener UID 4242 nos dará el token

- Vamos a ver un poco por dentro el codigo con ghidra
    ```c
    void main(void)

    {
      __uid_t _Var1;
      undefined4 uVar2;
      
      _Var1 = getuid();
      if (_Var1 != 0x1092) {
        _Var1 = getuid();
        printf("UID %d started us but we we expect %d\n",_Var1,0x1092);
                        /* WARNING: Subroutine does not return */
        exit(1);
      }
      uVar2 = ft_des("boe]!ai0FB@.:|L6l@A?>qJ}I");
      printf("your token is %s\n",uVar2);
      return;
    }
    ```

- Vemos que efectivamente si tenemos 4242 como uid nos dará el token

- Vamos a `gdb`:
    ```bash
    gdb level13
    b main
    r
    disassemble
    [...]
    0x0804859a <+14>:	cmp    $0x1092,%eax
    [...]
    b *0x0804859a
    c
    p $eax=0x1092
    c
    your token is 2A31L79asukciNyi8uppkEuSx
    [Inferior 1 (process 2247) exited with code 050]
    ```

- Lo tenemos
