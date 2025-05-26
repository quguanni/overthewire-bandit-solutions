# bandit.labs.overthewire.org
Tutorial for Bandit.Labs.Overthewire

bandit0: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

bandit1: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx: to open the file called - i have to specify the full directory: ./-

bandit2: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
use " " for "spaces in this filename"

bandit3: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
ls -a to show the hidden files

bandit4: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
cat ./-file07 is the file with the password to this level.
We can do file ./* instead to help find out which one is the file with the ASCII text

bandit5: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
./maybehere07/.file2cd

bandit6: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
using the command: find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null
notice 0 = stdin: standard input, 1 = stdout: standard output, 2 = stderr: standard error
remark: /dev/null is a blackhole

bandit7: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
grep "millionth" data.txt

bandit8: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
sort data.txt | uniq -u

uniq -d shows only duplicates
uniq -c shows the count of each line
uniq -u shows the lines that only appear once


bandit9: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
strings data.txt

bandit10: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
base64 -d data.txt

bandit11: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
rotate everything by 13 characters

bandit12: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
woww that was a lot.
1. create a temp directory and folder to have all this  happen and play with, mktemp -d
2. copy the data.txt into the temp directory: cp data.txt /tmp/tmp.nOxexKOMyE
3. rename it something else:
mv data.txt layer1
cp layer1 data.txt
4. then start to file the files to find out what type file that is: file layer2, which showed that it was an ASCII text
file data.txt
5. to remove the hexdump:
xxd -r data.txt >layer1
6. file layer1
which shoes that layer1 is gzip compressed data

7. mv layer1 layer1.gz
gunzip layer1.gz
8. file layer1, shows that the file is gzip 2 compressed data
9. mv layer1 layer1.gz
10. gunzip layer1.gz
11. file layer1, bzip2
12. mv layer1 layer1.bz2
13. bunzip2 layer1.bz2
etc. until we file layer1 and see that itis POSIX tar archieve (GNU)

14. mv layer1 layer1.tar
tar -xf layer1.tar
ls (we find a new file called data5.bin)
file data5.bin
mv data5.bin data5.tar
tar -xf data5.tar


bandit 13: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
This is a fun one and I love it!
Basically i know where the file is located and i wanna find it but i don't have the access to the file.
So basically the file is locked for the Bandit14user but i have the private key to become the bandit 14 user.
ssh bandit14@localhost -i sshkey.private -p 2220
cat /etc/bandit_pass/bandit14

bandit14: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
so i need to connect to port 30000
cat /etc/bandit_pass/bandit14 | nc localhost 30000


bandit15: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
echo 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo |  openssl s_client -connect localhost:30001 -quiet

bandit16:
nmap -p31000-32000 localhost
echo 'kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx' | nc localhost 31046
openssl s_client -connect localhost:31518 -quiet
echo 'kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx' | nc localhost 31518
echo 'kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx' | openssl s_client -connect localhost:31518 -quiet
echo 'kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx' | openssl s_client -connect localhost:31691 -quiet
echo 'kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx' | openssl s_client -connect localhost:31790 -quiet
RSA PRIVATE KEY:
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
copy and paste this whole thing into key.txt on the local machine (exit the ssh and save it on the machine as key.txt)

chmod 600 key.txt
ssh -i key.txt bandit17@bandit.labs.overthewire.org -p 2220

bandit17: x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
ls -a
diff passwords.new passwords.old
< x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
---
> C6XNBdYOkgt5ARXESMKWWOUwBeaIQZ0Y
grep 'C6XNBdYOkgt5ARXESMKWWOUwBeaIQZ0Y' passwords.old


bandit18: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"

bandit19: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO

first log in with the bandit18 passwords, then see what files and what their permissions are:
ls -al
we get -rwsr-x---  1 bandit20 bandit19 14884 Apr 10 14:23 bandit20-do                                    
We find that the only file with the s in place of x is the file called bandit20-d0, and this file gives us the user id permission as bandit20
that means we could use this file to access the locked bandit20 content
./bandit20-do cat /etc/bandit_pass/bandit20
