# Linux Command Line Capture The Flag Journey
Here, i show my journey through the 7 challenges of the Linux Command Line capture the flag challenge. All flags are in the format 'CTF{some_text_here}'

# Environment Setup
This CTF challenge required me to deploy a lab environment in my preferred cloud provider. Everything was automated, and I followed the individual guides to set up the environment before proceeding with the CTF Challenges. I started by cloning the ltc-linux-challenge repo and running the terraform file in azure/ 

sh

git clone https://github.com/learntocloud/ltc-linux-challenge
cd ltc-linux-challenge/azure


# Challenge 1:The Hidden File 

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