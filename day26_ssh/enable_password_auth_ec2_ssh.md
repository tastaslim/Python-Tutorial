# How to Enable Password Authentication in AWS ec2 Instances #

**The configuration to enable password authentication in AWS instance:-**

1. Log in to the server using ssh client of your choice using the private key.
    ```bash
    ssh -i your-key.pem username@ip_address
    ```
2. Set up a password for the user using passwd command along with the username.
   ```bash
   sudo passwd ec2-user # If machine is Amazon Linux
   sudo passwd ubuntu # If machine is Ubuntu
   ```
3. Open the sshd_config file.
   ```bash 
   sudo vi /etc/ssh/sshd_config
   ```
4. Find the Line containing “PasswordAuthentication” parameter and change its value from “no” to “yes”
   **PasswordAuthentication yes**
   If you want to set up “root” login, find “PermitRootLogin” parameter and change its value from “prohibit-password” to
   “yes”
5. Now, restart the “sshd” service using the following command.
   ```bash
   sudo service sshd restart
   ```
6. Now you can log out and log in using the password you set for the user.
   ```bash
   ssh ec2-user@ip_address
   # ssh ubuntu@15.1.25.40
   ```