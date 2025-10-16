# OverTheWire Bandit — Clean, Fast Solutions (0–34) + Concepts

> Fast, reusable walkthrough emphasizing **commands, concepts, and safe habits**.  
> **No hard-coded passwords or keys.** Copy/paste friendly and spoiler-minimal.

> **For lawful education only**; do not use against systems you don’t own/operate or have explicit permission to test.
---

## Table of contents
- [How to use this guide](#how-to-use-this-guide)
- [Quick reference (you’ll use these a lot)](#quick-reference-youll-use-these-a-lot)
- [Levels 0→24](#levels-024)
  - [0→1](#l0-1) • [1→2](#l1-2) • [2→3](#l2-3) • [3→4](#l3-4) • [4→5](#l4-5) • [5→6](#l5-6) • [6→7](#l6-7) • [7→8](#l7-8) • [8→9](#l8-9) • [9→10](#l9-10) • [10→11](#l10-11) • [11→12](#l11-12) • [12→13](#l12-13) • [13→14](#l13-14) • [14→15](#l14-15) • [15→16](#l15-16) • [16→17](#l16-17) • [17→18](#l17-18) • [18→19](#l18-19) • [19→20](#l19-20) • [20→21](#l20-21) • [21→22](#l21-22) • [22→23](#l22-23) • [23→24](#l23-24)
- [Levels 24→34](#levels-24-34)
  - [24→25](#l24-25) • [25→26](#l25-26) • [26→27](#l26-27) • [27→28 (git)](#l27-28) • [28→29 (git history)](#l28-29) • [29→30 (git tags)](#l29-30) • [30→31 (git branches)](#l30-31) • [31→32 (git push hook)](#l31-32) • [32→33 (git policy)](#l32-33) • [33→34](#l33-34)

---

## How to use this guide
- **Never paste real passwords/keys** into public docs. When you *already* have access, prefer variables like:
  ```bash
  PW14=$(cat /etc/bandit_pass/bandit14)
  ```
- **Environment**:
  ```bash
  export HOST=bandit.labs.overthewire.org
  export PORT=2220
  ```
- **Login template**:
  ```bash
  ssh bandit$N@$HOST -p $PORT
  ```
- **Helper** (optional):
  ```bash
  login(){ ssh bandit$1@$HOST -p $PORT; }
  ```
- **Tip**: If SSH acts weird (rare), try:
  ```bash
  ssh -o PreferredAuthentications=publickey,password -o PubkeyAuthentication=no …
  ```

---

## Quick reference (you’ll use these a lot)
- **Quoting**: `"path with spaces"` or `spaces\ in\ this\ filename`
- **Pipes**: `A | B` sends A’s stdout → B’s stdin
- **Redirection**: `>` overwrite, `>>` append, `<` stdin from file
- **Streams**: `0=stdin`, `1=stdout`, `2=stderr` (e.g., `2>/dev/null`)
- **Search**:
  - `grep -n PATTERN file`
  - `find DIR -type f -size 33c -user X -group Y -exec cat {} +`
- **Inspection/encoding**: `file`, `strings`, `base64 -d`, `tr`
- **Compression**: `gunzip`, `bunzip2`, `unxz`, `tar -xf`
- **Net**: `nc -lvp <port>`, `openssl s_client -connect host:port -quiet`
- **SSH**: `ssh -i key.pem user@host -p 2220` + `chmod 600 key.pem`

---

## Levels 0→24

<a id="l0-1"></a>
<details><summary><strong>Level 0 → 1</strong> — read <code>readme</code></summary>

**Cmds**
```bash
ls -l
cat readme
```
**Concepts**: `ls`, `cat`, relative paths.
</details>

<a id="l1-2"></a>
<details><summary><strong>Level 1 → 2</strong> — filename is <code>-</code></summary>

**Cmds**
```bash
cat ./-
# or
cat -- -
```
**Concepts**: Leading `-` looks like a flag; neutralize with `./` or `--`.
</details>

<a id="l2-3"></a>
<details><summary><strong>Level 2 → 3</strong> — spaces in filename</summary>

**Cmds**
```bash
cat "spaces in this filename"
# or
cat spaces\ in\ this\ filename
```
**Concepts**: Quoting/escaping.
</details>

<a id="l3-4"></a>
<details><summary><strong>Level 3 → 4</strong> — hidden file</summary>

**Cmds**
```bash
cd inhere
ls -a
cat .hidden
```
**Concepts**: Dotfiles, `ls -a`.
</details>

<a id="l4-5"></a>
<details><summary><strong>Level 4 → 5</strong> — locate the ASCII file</summary>

**Cmds**
```bash
cd inhere
file ./* | grep -i "ascii" | cut -d: -f1 | xargs -r cat
```
**Concepts**: `file`, pipelines, `xargs`.
</details>

<a id="l5-6"></a>
<details><summary><strong>Level 5 → 6</strong> — find by constraints</summary>

**Cmds**
```bash
find . -type f -size 1033c -readable ! -executable -print
# Then read the printed path:
cat ./<the_path_you_found>
```
**Concepts**: `find` filters (bytes vs. blocks), `! -executable`, `-readable`.
</details>

<a id="l6-7"></a>
<details><summary><strong>Level 6 → 7</strong> — search from <code>/</code></summary>

**Cmds**
```bash
find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null -exec cat {} +
```
**Concepts**: Absolute search; silence permission errors with `2>/dev/null`.  
**Streams**: `0=stdin`, `1=stdout`, `2=stderr`. `/dev/null` discards.
</details>

<a id="l7-8"></a>
<details><summary><strong>Level 7 → 8</strong> — grep a specific line</summary>

**Cmds**
```bash
grep -n "millionth" data.txt
```
**Concepts**: `grep` basics.
</details>

<a id="l8-9"></a>
<details><summary><strong>Level 8 → 9</strong> — unique line</summary>

**Cmds**
```bash
sort data.txt | uniq -u
# uniq -d (dups), uniq -c (counts)
```
**Concepts**: `sort` + `uniq`.
</details>

<a id="l9-10"></a>
<details><summary><strong>Level 9 → 10</strong> — inspect binary-ish data</summary>

**Cmds**
```bash
strings data.txt | less
```
**Concepts**: `strings` → printable sequences.
</details>

<a id="l10-11"></a>
<details><summary><strong>Level 10 → 11</strong> — base64 decode</summary>

**Cmds**
```bash
base64 -d data.txt
```
**Concepts**: Encodings, `-d`.
</details>

<a id="l11-12"></a>
<details><summary><strong>Level 11 → 12</strong> — ROT13</summary>

**Cmds**
```bash
tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt
```
**Concepts**: `tr` maps.
</details>

<a id="l12-13"></a>
<details><summary><strong>Level 12 → 13</strong> — un-hexdump, decompress iteratively</summary>

**Fast path**
```bash
mkdir -p "$(mktemp -d)" && cd $_
cp ~/data.txt .
xxd -r data.txt > layer

# Loop until "ASCII text" appears
while :; do
  if   file layer | grep -qi 'gzip';  then mv layer layer.gz;  gunzip -f layer.gz;  mv layer layer
  elif file layer | grep -qi 'bzip2'; then mv layer layer.bz2; bunzip2 -f layer.bz2; mv layer layer
  elif file layer | grep -qi 'xz';    then mv layer layer.xz;  unxz -f layer.xz;   mv layer layer
  elif file layer | grep -qi 'tar';   then mv layer layer.tar; mkdir t && tar -xf layer.tar -C t && rm -f layer.tar && mv t/* layer && rmdir t
  else break; fi
done
file layer && cat layer
```
**Concepts**: `xxd -r`, compression tools, `file` as a compass.
</details>

<a id="l13-14"></a>
<details><summary><strong>Level 13 → 14</strong> — SSH with provided key</summary>

**Cmds**
```bash
chmod 600 sshkey.private
ssh -i sshkey.private bandit14@localhost -p $PORT
cat /etc/bandit_pass/bandit14
```
**Concepts**: SSH identities, strict key perms (`600`).
</details>

<a id="l14-15"></a>
<details><summary><strong>Level 14 → 15</strong> — netcat to port 30000</summary>

**Cmds**
```bash
PW14=$(cat /etc/bandit_pass/bandit14)
echo "$PW14" | nc localhost 30000
```
**Concepts**: `nc`, pipelines.
</details>

<a id="l15-16"></a>
<details><summary><strong>Level 15 → 16</strong> — TLS on 30001</summary>

**Cmds**
```bash
PW15=$(cat /etc/bandit_pass/bandit15)
echo "$PW15" | openssl s_client -connect localhost:30001 -quiet
```
**Concepts**: `openssl s_client` (TLS).
</details>

<a id="l16-17"></a>
<details><summary><strong>Level 16 → 17</strong> — scan 31000–32000; find TLS that returns an SSH key</summary>

**Cmds**
```bash
PW16=$(cat /etc/bandit_pass/bandit16)
# Get open ports from nmap and probe them:
for p in $(nmap -p31000-32000 localhost -sT --open -oG - | awk '/open/{print $2}' | sed 's/[^0-9]/ /g'); do
  echo "$PW16" | openssl s_client -connect localhost:$p -quiet 2>/dev/null
done
# Save the PEM block (when you see it) to key.txt, then:
chmod 600 key.txt
ssh -i key.txt bandit17@$HOST -p $PORT
```
**Concepts**: Port scan → TLS probe; PEM hygiene.  
**Safety**: Don’t publish the key; store it locally with `600` perms.
</details>

<a id="l17-18"></a>
<details><summary><strong>Level 17 → 18</strong> — find the changed line</summary>

**Cmds**
```bash
diff passwords.new passwords.old
# The changed line is the new password
```
**Concepts**: Minimal diffs.
</details>

<a id="l18-19"></a>
<details><summary><strong>Level 18 → 19</strong> — non-interactive SSH</summary>

**Cmds**
```bash
ssh bandit18@$HOST -p $PORT "cat readme"
```
**Concepts**: Remote one-off commands via SSH.
</details>

<a id="l19-20"></a>
<details><summary><strong>Level 19 → 20</strong> — SUID helper</summary>

**Cmds**
```bash
ls -al
./bandit20-do cat /etc/bandit_pass/bandit20
```
**Concepts**: SUID binaries, privilege boundaries.
</details>

<a id="l20-21"></a>
<details><summary><strong>Level 20 → 21</strong> — local TCP handshake</summary>

**Cmds**
```bash
# Terminal A (listener)
nc -lvp 40000
# Terminal B (runner)
./suconnect 40000
# Paste bandit20 password into A; response comes back after B validates.
```
**Concepts**: Listener vs client; simple handshake.
</details>

<a id="l21-22"></a>
<details><summary><strong>Level 21 → 22</strong> — read cron + helper script</summary>

**Cmds**
```bash
cd /etc/cron.d
cat cronjob_bandit22
cat /usr/bin/cronjob_bandit22.sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```
**Concepts**: Cron → script → temp file.
</details>

<a id="l22-23"></a>
<details><summary><strong>Level 22 → 23</strong> — md5 of a specific phrase</summary>

**Cmds**
```bash
cd /etc/cron.d && cat cronjob_bandit23
cat /usr/bin/cronjob_bandit23.sh
echo -n "I am user bandit23" | md5sum | cut -d" " -f1
cat /tmp/<that_hash>
```
**Concepts**: Hash pipelines; exact spacing matters.
</details>

<a id="l23-24"></a>
<details><summary><strong>Level 23 → 24</strong> — drop a script into cron spool</summary>

**Cmds**
```bash
cd /var/spool/bandit24/foo
cat /usr/bin/cronjob_bandit24.sh

# Minimal script to copy the password:
cat > get24.sh <<'EOF'
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/b24
EOF
chmod +x get24.sh
# Wait up to 60s for cron to run, then:
cat /tmp/b24
```
**Concepts**: Cron exec context, ownership checks, absolute paths.  
**Fixed pitfall**: Use `/etc/bandit_pass/bandit24` (not `bandit_pass24`).
</details>

---

## Levels 24–34

> **Git levels** clone pattern:  
> `git clone ssh://banditNN-git@localhost/home/banditNN-git/repo`  
> Use the password of **banditNN** when prompted.

<a id="l24-25"></a>
<details><summary><strong>Level 24 → 25</strong> — brute-force a 4-digit PIN on <code>localhost:30002</code></summary>

**Goal**: Send `<password> <PIN>` on one line.

**Cmds**
```bash
PW24=$(cat /etc/bandit_pass/bandit24)
seq -w 0000 9999 | xargs -I{} echo "$PW24 {}" | nc localhost 30002 | tee out.txt
grep -v "Wrong!" out.txt
```
**Concepts**: Brute forcing with `seq -w`, piping to `nc`, capturing with `tee`.
</details>

<a id="l25-26"></a>
<details><summary><strong>Level 25 → 26</strong> — restricted shell via <code>showtext</code>; escape to <code>vim</code></summary>

**Cmds**
```bash
chmod 600 bandit26.sshkey
# Make your terminal small so the pager is interactive:
ssh -i bandit26.sshkey bandit26@localhost -p $PORT
# In the pager, press 'v' to open vim, then:
:e /etc/bandit_pass/bandit26
# or spawn a shell:
:set shell=/bin/bash | :shell
```
**Concepts**: Pager → `vim` escape; `:e` and `:shell`.
</details>

<a id="l26-27"></a>
<details><summary><strong>Level 26 → 27</strong> — SUID helper again</summary>

**Cmds**
```bash
ls -al
./bandit27-do cat /etc/bandit_pass/bandit27
```
**Concepts**: SUID execution.
</details>

<a id="l27-28"></a>
<details><summary><strong>Level 27 → 28</strong> — Git: clone & read</summary>

**Cmds**
```bash
mkdir -p /tmp/b27 && cd /tmp/b27
git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
cd repo && ls -la
cat README
```
**Concepts**: SSH remotes, temp workdirs.
</details>

<a id="l28-29"></a>
<details><summary><strong>Level 28 → 29</strong> — Git: recover from history</summary>

**Cmds**
```bash
mkdir -p /tmp/b28 && cd /tmp/b28
git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
cd repo
git log --oneline --decorate --graph
git show HEAD~1:README
# or
git log -p README
```
**Concepts**: `git show <commit>:<path>`, history diffs.
</details>

<a id="l29-30"></a>
<details><summary><strong>Level 29 → 30</strong> — Git: annotated tag</summary>

**Cmds**
```bash
mkdir -p /tmp/b29 && cd /tmp/b29
git clone ssh://bandit29-git@localhost/home/bandit29-git/repo
cd repo
git tag -n
git show secret   # if the tag is named 'secret' (check list)
```
**Concepts**: Tags carry messages/content.
</details>

<a id="l30-31"></a>
<details><summary><strong>Level 30 → 31</strong> — Git: other branch</summary>

**Cmds**
```bash
mkdir -p /tmp/b30 && cd /tmp/b30
git clone ssh://bandit30-git@localhost/home/bandit30-git/repo
cd repo
git branch -a
git checkout origin/dev   # for example
cat README
```
**Concepts**: Remote branches; detached HEAD checkouts.
</details>

<a id="l31-32"></a>
<details><summary><strong>Level 31 → 32</strong> — Git: push hook expects a specific file/content</summary>

**Cmds**
```bash
mkdir -p /tmp/b31 && cd /tmp/b31
git clone ssh://bandit31-git@localhost/home/bandit31-git/repo
cd repo
echo "May I come in?" > key.txt
git add key.txt && git commit -m "Add key.txt"
git push origin master 2>&1 | tee push.out
grep -iE "pass|password|bandit32" push.out
```
**Concepts**: Server-side hooks; capture push output.
</details>

<a id="l32-33"></a>
<details><summary><strong>Level 32 → 33</strong> — Git: satisfy policy (branch/message/tag)</summary>

**Cmds (systematic approach)**
```bash
mkdir -p /tmp/b32 && cd /tmp/b32
git clone ssh://bandit32-git@localhost/home/bandit32-git/repo
cd repo
cat README  # explains the policy

# Try common policies if terse:
git checkout -b feature
echo ok > proof.txt && git add proof.txt && git commit -m "feature: proof"
git push origin feature 2>&1 | tee push.out

git commit --allow-empty -m "please let me in"
git push 2>&1 | tee -a push.out

git tag request
git push origin request 2>&1 | tee -a push.out

grep -iE "pass|password|bandit33" push.out
```
**Concepts**: Branch vs tag policies, commit message checks.
</details>

<a id="l33-34"></a>
<details><summary><strong>Level 33 → 34</strong> — final note</summary>

**Cmds**
```bash
ls -la ~
# If prior output points to a file, read it:
# cat /etc/bandit_pass/bandit34
```
**Concepts**: Some installs end at 33; others include a final read/ack.
</details>

