default: help

.PHONY: all clean

help: # Show help
	@grep -E '^[_/a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

docker_image: # Build docker image 
	docker build -t discord-bot:latest .

run_docker: # Run docker container
	docker run -d -p 8000:8000 discord-bot:latest

update_run: docker_image run_docker # Update docker image and run container
