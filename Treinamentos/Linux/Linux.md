##### Pré requisitos

Veja [Docker Install](https://docs.docker.com/docker-for-windows/install/) **Logar e docker estar com status running**



##### Ubuntu docker

```
docker search ubuntu
```
```
docker pull ubuntu
```
```
docker images
```
```
docker ps -l
```
```
docker run ubuntu
```
```
docker run -i -t ubuntu /bin/bash
```

##### Referência - https://www.linuxpro.com.br/dl/guia_500_comandos_Linux.pdf

##### Listando conteudo
```
ls (list directory contents)

root@3c435b57cbf2:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```
```
ls -ltrh

root@3c435b57cbf2:/# ls -ltrh
total 64K
drwxr-xr-x   8 root root 4.0K May 23  2017 lib
drwxr-xr-x   2 root root 4.0K Apr 24  2018 home
drwxr-xr-x   2 root root 4.0K Apr 24  2018 boot
drwxr-xr-x   1 root root 4.0K Mar 11 21:03 usr
drwxr-xr-x   2 root root 4.0K Mar 11 21:03 srv
drwxr-xr-x   2 root root 4.0K Mar 11 21:03 opt
drwxr-xr-x   2 root root 4.0K Mar 11 21:03 mnt
drwxr-xr-x   2 root root 4.0K Mar 11 21:03 media
drwxr-xr-x   2 root root 4.0K Mar 11 21:03 lib64
drwxr-xr-x   1 root root 4.0K Mar 11 21:05 var
drwx------   2 root root 4.0K Mar 11 21:05 root
drwxr-xr-x   2 root root 4.0K Mar 11 21:05 bin
drwxrwxrwt   2 root root 4.0K Mar 11 21:05 tmp
drwxr-xr-x   1 root root 4.0K Mar 20 19:20 sbin
drwxr-xr-x   1 root root 4.0K Mar 20 19:20 run
drwxr-xr-x   1 root root 4.0K Apr 16 00:10 etc
dr-xr-xr-x 125 root root    0 Apr 16 00:10 proc
dr-xr-xr-x  13 root root    0 Apr 16 00:10 sys
drwxr-xr-x   5 root root  360 Apr 16 00:10 dev
```
```
ls -ltrhF

root@3c435b57cbf2:/# ls -ltrhf
lib  dev  opt  boot  root  media  sbin  sys  ..  mnt  .  tmp  home  run  srv  etc  usr  proc  var  bin  lib64  .dockerenv
```
```
ls -la

root@3c435b57cbf2:/# ls -la
total 72
drwxr-xr-x   1 root root 4096 Apr 16 00:10 .
drwxr-xr-x   1 root root 4096 Apr 16 00:10 ..
-rwxr-xr-x   1 root root    0 Apr 16 00:10 .dockerenv
drwxr-xr-x   2 root root 4096 Mar 11 21:05 bin
drwxr-xr-x   2 root root 4096 Apr 24  2018 boot
drwxr-xr-x   5 root root  360 Apr 16 00:10 dev
drwxr-xr-x   1 root root 4096 Apr 16 00:10 etc
drwxr-xr-x   2 root root 4096 Apr 24  2018 home
drwxr-xr-x   8 root root 4096 May 23  2017 lib
drwxr-xr-x   2 root root 4096 Mar 11 21:03 lib64
drwxr-xr-x   2 root root 4096 Mar 11 21:03 media
drwxr-xr-x   2 root root 4096 Mar 11 21:03 mnt
drwxr-xr-x   2 root root 4096 Mar 11 21:03 opt
dr-xr-xr-x 125 root root    0 Apr 16 00:10 proc
drwx------   2 root root 4096 Mar 11 21:05 root
drwxr-xr-x   1 root root 4096 Mar 20 19:20 run
drwxr-xr-x   1 root root 4096 Mar 20 19:20 sbin
drwxr-xr-x   2 root root 4096 Mar 11 21:03 srv
dr-xr-xr-x  13 root root    0 Apr 16 00:44 sys
drwxrwxrwt   2 root root 4096 Mar 11 21:05 tmp
drwxr-xr-x   1 root root 4096 Mar 11 21:03 usr
drwxr-xr-x   1 root root 4096 Mar 11 21:05 var
```

##### Navegando nos diretórios
```
cd (change directory)

root@3c435b57cbf2:/# cd home/
root@3c435b57cbf2:/home#

root@3c435b57cbf2:/home# cd ..
root@3c435b57cbf2:/#

```
##### Exibindo mensagem no terminal
```
echo (display a line of text)

root@3c435b57cbf2:/# echo ~
/root

root@3c435b57cbf2:/home# echo Essa mensagem passa cinco argumentos
Essa mensagem passa cinco argumentos

root@3c435b57cbf2:/home# echo "A mensagem entre aspas passa um argumento"
A mensagem entre aspas passa um argumento
```

##### Retornando o diretório em que estamos
```
pwd ( print name of current/working directory)

root@3c435b57cbf2:/home# pwd
/home

```

##### Criando arquivo
```
touch (change file timestamps)

root@3c435b57cbf2:/home# touch teste.txt
root@3c435b57cbf2:/home#
```

##### Confira o arquivo criado 
```
root@3c435b57cbf2:/home# ls -ltrh
total 0
-rw-r--r-- 1 root root 0 Apr 16 01:03 teste.txt
```

##### Criando arquivo com echo
```

root@3c435b57cbf2:/home# echo "Bem vindo!" > teste2.txt
root@3c435b57cbf2:/home#

root@3c435b57cbf2:/home# ls -ltrh
total 4.0K
-rw-r--r-- 1 root root  0 Apr 16 01:03 teste.txt
-rw-r--r-- 1 root root 11 Apr 16 01:08 teste2.txt  
```

##### Inserindo informações em um arquivo
```
root@3c435b57cbf2:/home# echo "Ola!" >> teste2.txt
root@3c435b57cbf2:/home#
```
##### Exibindo o conteúdo de um arquivo
```
cat (concatenate files and print on the standard output)

root@3c435b57cbf2:/home# cat teste2.txt
Bem vindo!
Ola!
```
##### Removendo arquivo
```
rm (remove files or directories)

root@3c435b57cbf2:/home# ls
teste.txt  teste2.txt

root@3c435b57cbf2:/home# rm teste.txt

root@3c435b57cbf2:/home# ls
teste2.txt

```
##### Criando diretorio
```
mkdir (make directories)

root@3c435b57cbf2:/home# mkdir workspace
root@3c435b57cbf2:/home# ls
teste2.txt  workspace
```
```
mkdir -p /temp/temp1/temp2
```
##### Copiando arquivo
```
cp (copy files and directories)

root@3c435b57cbf2:/home# ls
teste2.txt  workspace
root@3c435b57cbf2:/home# cp teste2.txt copiateste2.txt
root@3c435b57cbf2:/home# ls
copiateste2.txt  teste2.txt  workspace
```
##### Copiando para dentro de um diretório
```
root@3c435b57cbf2:/home# cp *txt workspace
root@3c435b57cbf2:/home# cd workspace/
root@3c435b57cbf2:/home/workspace# ls
copiateste2.txt  teste2.txt

```

##### Criando link simbolico
```
ln (make links between files)

ln -s

root@3c435b57cbf2:/# ln -s /home/workspace/dir1/ dir1

root@3c435b57cbf2:/# ls -l
total 72
drwxr-xr-x   2 root root 4096 Mar 11 21:05 bin
drwxr-xr-x   2 root root 4096 Apr 24  2018 boot
drwxr-xr-x   5 root root  360 Apr 16 00:10 dev
lrwxrwxrwx   1 root root   21 Apr 16 02:19 dir1 -> /home/workspace/dir1/
drwxr-xr-x   1 root root 4096 Apr 16 00:10 etc
drwxr-xr-x   1 root root 4096 Apr 16 02:17 home
drwxr-xr-x   8 root root 4096 May 23  2017 lib
drwxr-xr-x   2 root root 4096 Mar 11 21:03 lib64
drwxr-xr-x   2 root root 4096 Mar 11 21:03 media
drwxr-xr-x   2 root root 4096 Mar 11 21:03 mnt
drwxr-xr-x   2 root root 4096 Mar 11 21:03 opt
dr-xr-xr-x 125 root root    0 Apr 16 00:10 proc
drwx------   1 root root 4096 Apr 16 01:41 root
drwxr-xr-x   1 root root 4096 Mar 20 19:20 run
drwxr-xr-x   1 root root 4096 Mar 20 19:20 sbin
drwxr-xr-x   2 root root 4096 Mar 11 21:03 srv
dr-xr-xr-x  13 root root    0 Apr 16 00:44 sys
drwxr-xr-x   3 root root 4096 Apr 16 01:30 temp
drwxrwxrwt   2 root root 4096 Mar 11 21:05 tmp
drwxr-xr-x   1 root root 4096 Mar 11 21:03 usr
drwxr-xr-x   1 root root 4096 Mar 11 21:05 var
```
##### Utilizando o link simbolico

```
root@3c435b57cbf2:/# cd dir1

root@3c435b57cbf2:/dir1# pwd
/dir1
```
##### Movendo arquivo ou renomeando
```
mv (move - rename - files)

root@3c435b57cbf2:/home# ls
copiateste2.txt  teste2.txt  workspace

root@3c435b57cbf2:/home# mv teste2.txt workspace/
root@3c435b57cbf2:/home# ls
copiateste2.txt  workspace

root@3c435b57cbf2:/home# cd workspace
root@3c435b57cbf2:/home/workspace# ls
copiateste2.txt  dir1  teste2.txt

root@3c435b57cbf2:/home/workspace# mv -u teste2.txt  testerenomeado.txt
root@3c435b57cbf2:/home/workspace# ls
copiateste2.txt  dir1  testerenomeado.txt
```

##### Manipulacao de arquivo
```
echo 'linux' | cut -c 1-10

root@3c435b57cbf2:/home/workspace# echo 'uma simples string' | cut -c 1-17
uma simples strin
root@3c435b57cbf2:/home/workspace# echo 'uma simples string' | cut -c 1-10
uma simple
root@3c435b57cbf2:/home/workspace# echo 'uma simples string' | cut -c 1-2
um

```
```
grep (print lines mathing a pattern)
```

```
root@3c435b57cbf2:/home/workspace# touch states_br.csv
root@3c435b57cbf2:/home/workspace# vi status_br.csv
```


##### Usando o VI

[VICheatsheet](http://www.atmos.albany.edu/daes/atmclasses/atm350/vi_cheat_sheet.pdf)

```
esc+i (apertar tecla esc e tecla i)
copia o conteúdo abaixo
esc :x (apertar tecla esc e tecla : e x e apertar enter)
```

```
Sigla,Estado,Capital
AC,Acre,Rio Branco
AL,Alagoas,Maceió
AP,Amapá,Macapá
AM,Amazonas,Manaus
BA,Bahia,Salvador
CE,Ceara,Fortaleza
DF,Distrito Federal,Brasília
ES,Espírito Santo,Vitória
GO,Goiás,Goiânia
MA,Maranhão,São Luiz
MT,Mato Grosso,Cuiabá
MS,Mato Grosso do Sul,Campo Grande
MG,Minas Gerais,Belo Horizonte
PA,Pará,Belém
PB,Paraíba,João Pessoa
PR,Paraná,Curitiba
PE,Pernambuco,Recife
PI,Piauí,Terezina
RJ,Rio de Janeiro,Rio de Janeiro
RN,Rio Grande do Norte,Natal
RS,Rio Grande do Sul,Porto Alegre
RO,Rondônia,Porto Velho
RR,Roraima,Boa Vista
SC,Santa Catarina,Florianópolis
SP,São Paulo,São Paulo
SE,Sergipe,Aracajú
TO,Tocantins,Palmas
```



```
root@3c435b57cbf2:/home/workspace# cut -d, -f3 states_br.csv
```

```
Capital
Rio Branco
Maceió
Macapá
Manaus
Salvador
Fortaleza
Brasília
Vitória
Goiânia
São Luiz
Cuiabá
Campo Grande
Belo Horizonte
Belém
João Pessoa
Curitiba
Recife
Terezina
Rio de Janeiro
Natal
Porto Alegre
Porto Velho
Boa Vista
Florianópolis
São Paulo
Aracajú
Palmas
```

```
root@3c435b57cbf2:/home/workspace# wc states_br.csv
      27      56     662 states_br.csv
```

```
root@3c435b57cbf2:/home/workspace# wc -l states_br.csv
      27 states_br.csv
```

##### Detalhes do sistema

```
uname (print system information)

root@3c435b57cbf2:/home/workspace# uname -a
Linux 3c435b57cbf2 4.19.76-linuxkit #1 SMP Thu Oct 17 19:31:58 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
```

##### Mostrando o hostname
```
uname -n

root@3c435b57cbf2:/home/workspace# uname -n
3c435b57cbf2

hostname

root@3c435b57cbf2:/home/workspace# hostname
3c435b57cbf2
```

##### Mostrando há quanto tempo o sistema está rodando.
```
uptime (tell how long the system has been running)

root@3c435b57cbf2:/home/workspace# uptime
 03:09:38 up  7:38,  0 users,  load average: 0.00, 0.00, 0.00
```
```
Comando W
root@3c435b57cbf2:/home/workspace# w
18:49  up 1 day,  9:25, 2 users, load averages: 2.20 2.05 2.32
USER     TTY      FROM              LOGIN@  IDLE WHAT
diegolopes console  -                Wed09   33:24 -
diegolopes s000     -                18:32       - w
``` 
##### Mostrando a data e hora atual
```
date (print or set the system date and time)

root@3c435b57cbf2:/home/workspace# date
Thu Apr 16 03:10:57 UTC 2020
```

##### Mostrando calendário (não funciona no Docker)
```
cal (displays a calendar and the date of Easter)

~$ cal
     Abril 2020       
do se te qu qu se sá  
          1  2  3  4  
 5  6  7  8  9 10 11  
12 13 14 15 16 17 18  
19 20 21 22 23 24 25  
26 27 28 29 30   

```
##### rodando multiplos comandos
```
hostname; ls; date

root@3c435b57cbf2:/home/workspace# hostname; ls; date
3c435b57cbf2
copiateste2.txt  dir1  testerenomeado.txt
Thu Apr 16 03:23:04 UTC 2020	 
```



##### Checando distribuição do linux server

```
[root@hostname]# cat /etc/os-release


NAME="CentOS Linux"
VERSION="7 (Core)"
ID="centos"
ID_LIKE="rhel fedora"
VERSION_ID="7"
PRETTY_NAME="CentOS Linux 7 (Core)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:centos:centos:7"
HOME_URL="https://www.centos.org/"
BUG_REPORT_URL="https://bugs.centos.org/"

CENTOS_MANTISBT_PROJECT="CentOS-7"
CENTOS_MANTISBT_PROJECT_VERSION="7"
REDHAT_SUPPORT_PRODUCT="centos"
REDHAT_SUPPORT_PRODUCT_VERSION="7"

```


##### Procurando o arquivo kettle properties a partir do /

```
[root@hostname diegols]# find / -name states_br.csv 2>/dev/null


```
##### Encontrando a palavra PR no arquivo e trazendo 1 linhas antes e depois

```
diegolopes@MBP-de-Diego Downloads % grep PR states_br.csv 
PR,Paraná,Curitiba

diegolopes@MBP-de-Diego Downloads % grep -1 PR states_br.csv
PB,Paraíba,João Pessoa
PR,Paraná,Curitiba
PE,Pernambuco,Recife


```


##### Qual o diretorio estou
```
[root@hostname]# pwd

/home
```

##### Listando arquivos que terminam zip
```
(base) diegolopes@MBP-de-Diego Downloads % ls -ltrh *zip
-rw-r--r--  1 diegolopes  staff   9.8M Jan 19 21:40 Documentos Diego.zip
-rw-r--r--@ 1 diegolopes  staff   5.5M Jan 21 14:43 SR-Leg_ASC.zip
-rw-r--r--@ 1 diegolopes  staff   3.2K Jan 21 14:43 Essentials_Lesson_10_Files.zip
-rw-r--r--@ 1 diegolopes  staff   683B Jan 21 14:52 Essentials_Lesson_6_files_.zip

```


##### Listando as primeiras linhas com head

```
[root@hostname ]# head states_br.csv
Sigla,Estado,Capital
AC,Acre,Rio Branco
AL,Alagoas,Maceió
AP,Amapá,Macapá
AM,Amazonas,Manaus
BA,Bahia,Salvador
CE,Ceara,Fortaleza
DF,Distrito Federal,Brasília
ES,Espírito Santo,Vitória
GO,Goiás,Goiânia


```

##### Listando as ultimas 10 linhas com tail (tail -f *)
```
[root@hostname ]#  tail -10 states_br.csv 
PI,Piauí,Terezina
RJ,Rio de Janeiro,Rio de Janeiro
RN,Rio Grande do Norte,Natal
RS,Rio Grande do Sul,Porto Alegre
RO,Rondônia,Porto Velho
RR,Roraima,Boa Vista
SC,Santa Catarina,Florianópolis
SP,São Paulo,São Paulo
SE,Sergipe,Aracajú
TO,Tocantins,Palmas%                                      

```
##### Qual user estou logado
```
[diegols@hostname ~]$ whoami
diegols
```
##### Verificando o conteudo do arquivo com o cat
```
[root@hostname diegols]# ccat states_br.csv 
```
##### Listando o tamanho dos mounts
```
[diegols@hostname ~]$ df -h
Filesystem                    Size  Used Avail Use% Mounted on
devtmpfs                       63G     0   63G   0% /dev
tmpfs                          63G     0   63G   0% /dev/shm
tmpfs                          63G  234M   63G   1% /run
tmpfs                          63G     0   63G   0% /sys/fs/cgroup
/dev/mapper/rootvg-rootlv     976M  157M  753M  18% /
/dev/mapper/rootvg-usrlv      3.9G  3.3G  317M  92% /usr
/dev/sda1                     976M  271M  639M  30% /boot
/dev/mapper/rootvg-tmplv      976M  328M  582M  37% /tmp
/dev/mapper/rootvg-optlv      976M  476M  434M  53% /opt
/dev/mapper/rootvg-homelv     2.0G   60M  1.8G   4% /home
/dev/mapper/rootvg-varlv      2.0G  690M  1.2G  38% /var
/dev/mapper/appvg-wloglv      118G   91G   22G  81% /work/prb
/dev/mapper/appvg-wpentaholv   99G  7.2G   87G   8% /work/pentaho
tmpfs                          13G     0   13G   0% /run/user/0
tmpfs                          13G     0   13G   0% /run/user/1005
```
##### Listando as 10 maiores pastas
```
[root@hostname diegols]# du -a /var | sort -n -r | head -n 10
699748  /var
472868  /var/cache
470468  /var/cache/yum
470464  /var/cache/yum/x86_64
470460  /var/cache/yum/x86_64/7
279992  /var/cache/yum/x86_64/7/REPOSITORIO-LOCAL
237888  /var/cache/yum/x86_64/7/REPOSITORIO-LOCAL/gen
237884  /var/cache/yum/x86_64/7/REPOSITORIO-LOCAL/gen/primary_db.sqlite
176876  /var/lib
153892  /var/lib/rpm
[root@hostname diegols]#
```
##### Checando quantidade de memoria em gigabytes
```

[root@hostname diegols]# free -g
              total        used        free      shared  buff/cache   available
Mem:            125           2          90           0          32         121
Swap:             1           0           1
```
##### Checando quantidade de memoria em megabytes
```
[root@hostname diegols]# free -m
              total        used        free      shared  buff/cache   available
Mem:         128771        2950       92107         363       33712      124849
Swap:          2047          29        2018
[root@hostname diegols]#
```