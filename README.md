# What is it?

[DroneCI](https://drone.io/) plugin that pulls images from [AWS ECR](https://aws.amazon.com/ecr/) (Amazon Elastic Container Registry)

# Why do I need it?

It can be used to auth against ECR, enabling drone to pull private images from there.

# Usage

## If you're using [kubernetes](https://kubernetes.io/) [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) auth

```
pipeline:
  pull:
    image: yspro/drone-plugin-ecr-fetcher
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    images:
      - $ecr_repo/public_image
      - $ecr_repo/private_image
      - $ecr_repo/another_private_image:some_tag
  ... your steps
```

## If you have AWS ENVs in secrets

```
pipeline:
  pull:
    image: yspro/drone-plugin-ecr-fetcher
    secrets: [aws_access_key_id, aws_secret_access_key]
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    images:
      - $ecr_repo/public_image
      - $ecr_repo/private_image
      - $ecr_repo/another_private_image:some_tag
  ... your steps
```

# Plugin parameters

## images (required)

That parameter is of `list` type where you specify your docker images

## aws_region (optional)

The name of the AWS region. By default it's set to `eu-central-1`.
