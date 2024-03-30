### LEVEL02
- ls -la
    ```bash
    [...]
    ----r--r-- 1 flag02  level02 8302 Aug 30  2015 level02.pcap
    [...]
    ```
- I found a file level02.pcap (wireshark) https://www.wireshark.org/
- I download the file locally.
    ```bash
    scp -p 4242 level02@192.168.1.42:/home/user/level02/level02.pcap .
    ```
- I open the file with Wireshark.
- While browsing through it, I see a packet containing the word `Password`
- I use the tshark command, which is like Wireshark but for the command line, to extract all the data.
    ```bash
    tshark -Tfields -e data.data -r level02.pcap | xxd -r -p
    [...]
    Password: ft_wandrNDRelL0L
    [...]
    ```
- I try the password but it doesn't work.
- It occurs to me to try a `cat -e`
    ```bash
    tshark -Tfields -e data.data -r level02.pcap | xxd -r -p | cat -e
    [...]
    Password: ft_wandr^?^?^?NDRel^?L0L^M^@^M$
    [...]
    ```
- It has non-printable characters.
- Searching through the data, I see that they correspond to 7f (DEL).
- Therefore, the password has `DEL` characters that need to be removed, resulting in `ft_waNDReL0L`


### LEVEL02

- ls -la
    ```bash
    [...]
    ----r--r-- 1 flag02  level02 8302 Aug 30  2015 level02.pcap
    [...]
    ```
- Encuentro un archivo `level02.pcap` (wireshark) https://www.wireshark.org/
- Descarco en local el archivo
    ```bash
    scp -p 4242 level02@192.168.1.42:/home/user/level02/level02.pcap .
    ```
- Abro el archivo con wireshark
- Navegando por el veo un paquete que contiene la palabra `Password`
- Utilizo el comando tshark que el wireshark pero en linea de comandos para sacar toda la data
    ```bash
    tshark -Tfields -e data.data -r level02.pcap | xxd -r -p
    [...]
    Password: ft_wandrNDRelL0L
    [...]
    ```
- Pruebo la clave pero no funciona
- Se me ocurre hacer un `cat -e` 
    ```bash
    tshark -Tfields -e data.data -r level02.pcap | xxd -r -p | cat -e
    [...]
    Password: ft_wandr^?^?^?NDRel^?L0L^M^@^M$
    [...]
    ```
- Tiene caracteres no imprimibles
- Buscando en la data veo que coresponden a 7f(DEL)
- Por lo cual la pass tiene caracteres `DEL` que hay que quitar quedando `ft_waNDReL0L`  

