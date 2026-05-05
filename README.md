# Cloud-devops-final-project
Deploying full stack web application


Part 1:
1. Create an account on docker hub using your personal email
2. Create a frontend application that displays a webpage. The dockerfile will be something
similar to the image below:
3. Create a flask based application for the backend using python. Start with the hello
application here https://www.digitalocean.com/community/tutorials/how-to-make-
aweb-application-using-flask-in-python-3#step-2-creating-a-base-application and create
a base application
4. Modify the application such that it can display a .jpg image

-----------------------------------------------------------------------------------------------------------------------------------------
Part 2:
1. Containerize the flask based application from Part 1. Now you should have two
Dockerfiles, one for frontend, one for backend. YourDockerfile for backend will have
these lines.
• FROM python:3.10-slim: It begins with a slim official Python base image to
reduce the overall size.
• COPY requirements.txt .: The dependencies file is copied into the image
first.
• RUN pip install -r requirements.txt: Leveraging Docker's layer caching,
dependencies (which change infrequently) are installed in a separate step. This
step is only re-run
if requirements.txt changes.
• COPY . .: The application source code (app.py) is copied into the image.
• CMD ["python", "app.py"]: This defines the default command to execute
when a container is started from this image, launching the Flask application.
2. Build the images using docker build. You can use commands like those below once for
your frontend application and once for your backend application docker build -t your-
username/my-app:latest . docker push your-username/my-app:latest where, your-
username is your docker hub user name and my-app is your backend app
3. Run 2 containers, one for frontend, one for backend
----------------------------------------------------------------------------------------------------------------------------------------------
Part 3:
1. Deploy your backend flask application in a Kubernetes cluster using kubectl commands
on minikube
• Create a new object of type deployment.
• Name it backend.
• Use your backend docker image for the containers.
• Maintain 3 running replicas of the pod.
• Hint: Use kubectl create deployment command
• Use kubectl get pods --show-labels to verify that pods are successfully created
2. Deploy your frontend application with 4 replicas. Create a node.yaml file similar to the
one shown below:
Use kubectl apply to use this yaml file (find out the correct command line)
3. Use kubectl get pods and find out the label of one of the pods. (find out what flag is
needed to show the labels)
4. Create an endpoint using this command kubectl label pod <name-of-your-frontendpod>
run=testp
5. Find the name of the service using kubectl get svc
6. Find the endpoint ip address using kubectl describe svc <your service name>
7. A sample set of commands is given below:
8. Test the connection using curl or going to the ip address from a browser

