#!/bin/bash
docker stop catapult
docker rm catapult
docker pull scottpaulrichard/catapult
docker run -p 80:80 -d --name catapult scottpaulrichard/catapult
