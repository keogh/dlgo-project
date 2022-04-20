run:
	docker run -it --rm -v $(pwd):/root -p 8888:8888 -p 5000:5000 -v /tmp:/tmp keras

run-bash:
	docker run -it --rm -v $(pwd):/root -p 8888:8888 -p 5000:5000 -v /tmp:/tmp keras /bin/bash

build:
	docker build -t keras .
