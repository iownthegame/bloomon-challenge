## run
- run container: `docker run --name my-bloomon -d -t python-bloomon`
- access inside the container: `docker exec -it my-bloomon bin/bash`
- execute inside the container: `python program.py`
- paste input data to standard input
- show output data at standard output
- exit container: `exit`
- stop and remove container: `docker stop my-bloomon && docker rm my-bloomon`