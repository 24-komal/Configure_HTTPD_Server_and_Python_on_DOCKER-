import os
import subprocess

def takeCommand():
	query=input("Enter----->")
	return query

while True:
	print("Press enter to continue...")
	n=input("")
	os.system("clear")
	os.system("tput setaf 2")
	print("\n\t"+37*"-")
	print("\t\t\tMenu")
	print("\n\t"+37*"-")
	os.system("tput setaf 3")
	print("\n\tSelect an option: \n")
	os.system("tput setaf 7")
		
	print("\t1. Configure Docker tool")
	print("\t2. Pull an Image")
	print("\t3. Launch the Docker Container")
	print("\t4. Configure Apache Webserver")
	print("\t5. Write the code in Document root")
	print("\t6. Start Webserver services")
	print("\t7. Install Python Interpreter")
	print("\t8. Write Python Code")
	print("\t9. Run Python code")
	print("\t0. Exit\n")

	os.system("tput setaf 6")
	ch=int(input("Enter your Choice:"))
	os.system("tput setaf 7")

	if ch == 1:
		os.system("clear")
		print("*****************")
		x=subprocess.getstatusoutput("rpm -q docker-ce")
		if x[0]!=0:
			print("\tInstalling Docker...")
			f=open("/etc/yum.repos.d/docker-ce.repo","a")
			docrepo="[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0\n"
			f.write(docrepo)
			f.close()
			os.system("yum install docker-ce --nobest")
			os.system("systemctl start docker")
			os.system("systemctl enable docker")
			print("*****************")
		else:
			print("\tDocker is allready installed)
	elif ch == 2: 
		os.system("clear")
		print("*****************")
		print("Enter the Image name--->")		
		img=takeCommand()
		os.system("docker pull "+img)
		print("Your "+img+" image is been downloaded")
		print("*****************")
	
	elif ch == 3:
		os.system("clear")
		print("*****************")
		n=input("Enter the name:")
		p=input("\nEnter the Docker port no:")
		print("This port no is used to bind local port to Docker port so that you can expose your container to the outside world")
		os.system("sleep 3")
		print("\nThis are your available Images:-\n")
		os.system("docker images")
		os.system("sleep 2")
		print("\nWhich Image should i choose..?")
		imgs=takeCommand()
		print("\nYour new OS is been launched")
		os.system(f"docker run -it -p {p}:80 --name {n} {imgs}")		
		print("*****************")

	elif ch == 4:
		os.system("clear")
		print("*****************")
		n=input("Enter the container name you want to configure Webserver:")
		os.system(f"docker start {n}")
		os.system(f"docker exec -it {n} yum install httpd")
		os.system("yum install httpd -y")
		print("*****************")

	elif ch == 5:
		os.system("clear")
		print("*****************")
		n=input("Enter the container name where you want to write the code:")
		os.system(f"docker start {n}")
		q=input("Enter the file name with extension:")
		os.system(f"docker exec -it {n} touch /var/www/html/{q}")
		print("Write your code....")
		os.system("sleep 1")
		os.system(f"docker exec -it {n} vi /var/www/html/{q}")
		print("*****************")

	elif ch == 6:
		os.system("clear")
		print("*****************")
		n=input("Enter the container name where you want to start Webserver services:")
		os.system(f"docker start {n}")
		os.system(f"docker exec -it {n} /usr/sbin/httpd")
		print("*****************")

	elif ch == 7:
		os.system("clear")
		print("*****************")
		n=input("Enter the container name you want to install python:")
		os.system(f"docker start {n}")
		os.system(f" docker exec -it {n} yum install python3 -y")
		print("*****************")

	elif ch == 8:
		os.system("clear")
		print("*****************")
		n=input("Enter the container name where you want to write the code:")
		os.system(f"docker start {n}")
		q=input("Enter the file name with extension:")
		os.system(f"docker exec -it {n} touch /{q}")
		print("Write your code....")
		os.system("sleep 1")
		os.system(f"docker exec -it {n} vi /{q}")
		print("*****************")
		
	elif ch == 9:
		os.system("clear")
		print("*****************")
		n=input("Enter the container name where you want to run the code:")
		os.system(f"docker start {n}")
		q=input("Enter the file name with extension:")
		os.system(f"docker exec -it {n} python3 {q}")
		print("*****************")

	elif ch == 0:
		os.system("clear")
		print("*****************")
		print("****Thanks for using me****")
		print("*****************")
		break
	
	else:
		print("Please enter a valid option...")
				
		
		
		

