### LEVEL01
- There are no files in the home directory.
- I search for files belonging to flag01 but find nothing.
- I check the permissions of `/etc/passwd`
    ```
    cat /etc/passwd
    [...]
    flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
    [...]
    ```
- We have the key but it's encrypted.
- We copy it to the local machine.
    ```bash
    echo "flag01:42hDRfypTqqnw" > tocrack
    john tocrack --show
    flag01:abcdefg
    ```
- We'll use John to decrypt it https://www.openwall.com/john/

### LEVEL01
- No hay archivos en el home
- Busco archivos de flag01 y no encuentro nada
- Miro los permisos de `/etc/passwd`
    ```
    cat /etc/passwd
    [...]
    flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
    [...]
    ```
- Tenemos la clave pero está cifrada
- La copiamos en la maquina local
- Usaremos john para desencriptar https://www.openwall.com/john/
    ```bash
    echo "flag01:42hDRfypTqqnw" > tocrack
    john tocrack --show
    flag01:abcdefg
    ```
