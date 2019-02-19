#!/bin/sh
docker run -ti -v `pwd`/fakephotos:/usr/src/app/fakephotos fakephotos_dataset:latest
