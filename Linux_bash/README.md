# Linux Command Line Capture The Flag Journey
Here, i show my journey through the 7 challenges of the Linux Command Line capture the flag challenge. All flags are in the format 'CTF{some_text_here}'

# Environment Setup
This CTF challenge required me to deploy a lab environment in my preferred cloud provider. Everything was automated, and I followed the individual guides to set up the environment before proceeding with the CTF Challenges. I started by cloning the ltc-linux-challenge repo and running the terraform file in azure/ 

```sh
git clone https://github.com/learntocloud/ltc-linux-challenge
cd ltc-linux-challenge/azure

```


# Challenge 1 : The Hidden File 

**Objective:** Find a hidden file in the `ctf_challenges` directory and read its contents.

**Skills tested:**

- Understanding of hidden files in Linux
- Using `ls` with appropriate flags
- Reading file contents

I used ```ls -la``` to find the hidden file and used ```cat``` command to display the flag

flag 1-Found
ctf_user@ctf-vm:~/ctf_challenges$ cat .hidden_flag
CTF{finding_hidden_treasures}

## Challenge 2: The Secret File

**Objective:** Locate a file with the word "secret" in its name anywhere in the /home/ctf_user directory.

**Skills tested:**

- Recursive file searching
- Using grep or find commands

I used the ```find``` command to search for the file 

## Challenge 3: The Largest Log

**Objective:** Find the largest file in the /var/log directory and retrieve the flag from it.

**Skills tested:**

- Navigating directory structures
- Sorting and filtering files based on size
- Reading file contents

`cd /var/log
ls -s
tail -n 5 large_log_file.log`

## Challenge 4: The User Detective

**Objective:** Identify the user with UID 1002 and find the flag in their home directory.

**Skills tested:**

- Understanding user management in Linux
- Reading the /etc/passwd file or using id command
- Navigating to other users' home directories

I used ```grep 1002 /etc/passwd``` to search for the UID 1002 in the /etc/passwd.
I found the **ctf_user** but I could not cd into this directory even with sudo. I decided to list the files using sudo and was able to find the flag.txt which i ```sudo cat /home/flag_user/.profile``` and found the challenge 4 flag.

## Challenge 5: The Permissive File

**Objective:** Locate the file owned by root with permissions 777 and read its contents.

**Skills tested:**

- Understanding Linux file permissions
- Using find command with permission parameters
- Reading file contents as a non-root user

I used the ```find ``` command to look for a file ```-type f``` from root ```/``` with full permissions ```-perm 777```. I then ```cat /opt/systems/config/system.conf``` the file and found the flag

## Challenge 6: The Hidden Service

**Objective:** Find the process running on port 8080 and retrieve the flag from its command.

**Skills tested:**

- Using network-related commands (netstat, ss, or lsof)
- Understanding process information
- Reading process details

I used ```netstat``` to show any tcp/udp connections or listening sockets. then used grep to search through the output and find **:8080**. I retrieved the flag from `curl http://localhost:8080`

## Challenge 7: The Encoded Secret

**Objective:** Decode the base64 encoded flag in the 'encoded_flag.txt' file.

**Skills tested:**

- Understanding of base64 encoding
- Using command-line decoding tools

I used ```find ~/.ssh -type f``` command to find the encoded file, then used `cat /home/ctf_user/.ssh/secrets/backup/.authorized_keys `



