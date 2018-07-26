#!/usr/bin/env python

import os
import docker
import requests

def image_list():
    env_key = "PLUGIN_IMAGES"

    if os.environ.has_key(env_key):
        return os.environ[env_key].split(",")
    else:
        print "required " + env_key + " ENV variable is missing"
        exit(1)

def docker_client():
    try:
        client = docker.from_env()
        client.ping()
        return client
    except requests.exceptions.ConnectionError:
        print "Can't connect to Docker daemon. Make sure you shared the docker.sock"
        exit(1)

def pull_image(docker_client, image_name):
    try:
        image = image_name.split(":")
        if len(image) == 1: image.append("latest")
        print "pulling " + image[0] + ":" + image[1] + "..."
        docker_client.images.pull(image[0], image[1])
    except docker.errors.APIError as e:
        print e
        exit(1)

def main():
    client = docker_client()

    for docker_image in image_list():
        pull_image(client, docker_image)

    print "Done"

if __name__ == "__main__":
    main()
