- Tenemos un binario
level13@SnowCrash:~$ file level13
level13: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xde91cfbf70ca6632d7e4122f8210985dea778605, not stripped
- Ejecutamos y tenemos este output:
level13@SnowCrash:~$ ./level13
UID 2013 started us but we we expect 4242
- Al parece si conseguimos tener UID 4242 nos dará el token
- Vamos a ver un poco por dentro el codigo con ghidra
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
- Vemos que efectivamente si tenemos 4242 como uid nos dará el token
- Vamos a gdb:
    b main
    r
    disassemble
    [...]
    0x0804859a <+14>:	cmp    $0x1092,%eax
    [...]
    b *0x0804859a
    c
    p $eax=0x1092
    Continuing.
    your token is 2A31L79asukciNyi8uppkEuSx
    [Inferior 1 (process 2247) exited with code 050]
- Lo tenemos
