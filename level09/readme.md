### LEVEL09

- Two files in home
    ```bash
    -rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
    ----r--r-- 1 flag09 level09   26 Mar  5  2016 token
    ```

- Execute ./level09
    ```bash
    level09@SnowCrash:~$ ./level09
    You need to provied only one arg.
    level09@SnowCrash:~$ ./level09 token
    tpmhr
    ```

- Cat token
    ```bash
    level09@SnowCrash:~$ cat token
    f4kmm6p|=pnDBDu{
    ```

- It seems that the encryption affects the string of the argument and not the content of the file.

- I try some strings to see if I can find any logic in the encryption.
    ```bash
    level09@SnowCrash:~$ ./level09 HOLA
    HPND
    level09@SnowCrash:~$ ./level09 123456
    13579;
    level09@SnowCrash:~$ ./level09 1234
    1357
    level09@SnowCrash:~$ ./level09 9ABC
    9BDF
    ```

- It seems that the encryption is `c = c + position_in_array(c)`.

- I'll create a Python script to decrypt the token.   
    ```bash
    vi /tmp/a
    ```

    ```python
    #!/bin/python
    res = ""
    pos = 0

    f = open("/home/user/level09/token")
    code = f.read();
    for l in code:
        res += chr(ord(l) - pos)
        pos += 1
    print("DECODE TOKEN: ", res)
    ```

- Execute `/tmp/a`
    ```bash
    level09@SnowCrash:~$ chmod 755 /tmp/a
    level09@SnowCrash:~$ /tmp/a
    level09@SnowCrash:~$ /tmp/a
    Traceback (most recent call last):
    File "/tmp/a", line 9, in <module>
    res += chr(ord(l) - pos)
    ValueError: chr() arg not in range(256)
    ```

- We have a problem, which is that the character `\n` goes out of the ASCII table when subtracting a certain amount.

- Let's modify the script.
    ```python
    #!/bin/python
    res = ""
    pos = 0
    
    try:
        f = open("/home/user/level09/token")
        code = f.read();
        print("TO DECODE", code)
        for l in code:
            res += chr(ord(l) - pos)
            pos += 1
    except:
        print("DECODE TOKEN: ", res)
    ```

- Execute `/tmp/a`
    ```bash
    level09@SnowCrash:~$ /tmp/a
    ('TO DECODE', 'f4kmm6p|=\x82\x7fp\x82n\x83\x82DB\x83Du{\x7f\x8c\x89\n')
    ('DECODE TOKEN: ', 'f3iji1ju5yuevaus41q1afiuq')
    ```

---

### LEVEL09

- Dos archivos en el home
    ```bash
    -rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
    ----r--r-- 1 flag09 level09   26 Mar  5  2016 token
    ```

- Ejecuto ./level09
    ```bash
    level09@SnowCrash:~$ ./level09
    You need to provied only one arg.
    level09@SnowCrash:~$ ./level09 token
    tpmhr
    ```

- Cat a token
    ```bash
    level09@SnowCrash:~$ cat token
    f4kmm6p|=pnDBDu{
    ```

- Parece que el cifrado afecta al la string del argumento y no al contenido del archivo

- Pruebo alguna string para ver si encuentro alguna lógica en el cifrado
    ```bash
    level09@SnowCrash:~$ ./level09 HOLA
    HPND
    level09@SnowCrash:~$ ./level09 123456
    13579;
    level09@SnowCrash:~$ ./level09 1234
    1357
    level09@SnowCrash:~$ ./level09 9ABC
    9BDF
    ```

- Parece que el cifrado es `c = c + position_in_array(c)`

- hago un script python para desencriptar token
    ```bash
    vi /tmp/a
    ```

    ```python
    #!/bin/python
    res = ""
    pos = 0

    f = open("/home/user/level09/token")
    code = f.read();
    for l in code:
        res += chr(ord(l) - pos)
        pos += 1
    print("DECODE TOKEN: ", res)
    ```

- Ejecutamos /tmp/a
    ```bash
    level09@SnowCrash:~$ chmod 755 /tmp/a
    level09@SnowCrash:~$ /tmp/a
    level09@SnowCrash:~$ /tmp/a
    Traceback (most recent call last):
    File "/tmp/a", line 9, in <module>
    res += chr(ord(l) - pos)
    ValueError: chr() arg not in range(256)
    ```

- Tenemos un problema y es que el caracter `\n` al restarle una cantidad se sale de la tabla ASCII

- Modificamos el script
    ```python
    #!/bin/python
    res = ""
    pos = 0
    
    try:
        f = open("/home/user/level09/token")
        code = f.read();
        print("TO DECODE", code)
        for l in code:
            res += chr(ord(l) - pos)
            pos += 1
    except:
        print("DECODE TOKEN: ", res)

- Ejecutamos /tmp/a
    ```bash
    level09@SnowCrash:~$ /tmp/a
    ('TO DECODE', 'f4kmm6p|=\x82\x7fp\x82n\x83\x82DB\x83Du{\x7f\x8c\x89\n')
    ('DECODE TOKEN: ', 'f3iji1ju5yuevaus41q1afiuq')
    ```
