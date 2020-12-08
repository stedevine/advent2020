# runs the specified script in python 3.8.6 in a Docker container.
docker run -it --rm --name python_test -v "$PWD":/working -w /working python:3.8.6 python $1
