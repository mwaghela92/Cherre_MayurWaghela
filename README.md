Steps to execute the docker file in this repository:

	•	Fork the repository

	•	Copy the URL of the forked repository 

	•	Open terminal and navigate to a folder where you would want to clone the repository

	•	Clone the repository by typing the following command:
$ git clone <forked_repository_URL>

	•	Once the repository is cloned, you will see that all the files have been downloaded into the current directory. Now we have to build a docker image and run it to execute the files

	•	Navigate to the current directory (if not in the directory)
	
	•	Type the following docker commands in order to run the test_file.py and the Cherre01.py scripts
	
	

$docker image build -t <name_of_image> .

#This will create the docker image

$docker run –p 5000:5000 <name_of_image>

#This will create a container and run the scripts. You will see an address - http://0.0.0.0:5000/ in the logs. Go to the address and you will find the result of the required query exposed to the world


