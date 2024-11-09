# ICS Socket Servers

## Goals
The goal of this repo is to host simulated socket servers that emulate ICS's. This will provide current and future soldiers a training platform for interacting with virtualized equipment. Cheap, simple, and easy.

## Code
These socket servers are not to be written in any other language than python and must have had black run against them for formatting. A merge request or pull request will be denied if black the python formatter is not run against it. Variables need to refrain from profanity unless absolutely necessary to express just what clusterf*** you are trying to make. I would say you also need to type everything using MyPy but that would literally add 5 years to completing this repo. Keep the code clean, simple, and maintainable. And yes, if you have the opportunity to hide a meme or rickroll, do it if appropriate. Inappropriate commits are recorded on the git.mil site and will be handled accordingly.

## Devices and Vendors
Each vendor is hosted in a folder. Each folder contains a README.md with company/vendor information and PLC/ICS device information. This information is pulled from datasheets which contain things like command structure, communication protocols (IE MODBUS, TELNET), and known vulnerabilities. There will be a python script called [devicename][version] server.py and this script can be pulled down and used in a docker container or run on a host to simulate the PLC. A PLC server will also have known vulnerabilities. All support scripts (libs, makefiles for bins if needed, docker build scripts) will be in the vendors folder.

## Example
Reference here. This seemed to be a really good place to start. You can clone this repo and modify per device or find us new devices.

## Access
If you would like to support the 136 CSC DET 2 VTNG, please shoot a message to the owner. You can find him in the git history.
