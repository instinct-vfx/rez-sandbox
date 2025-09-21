# Rez development and testing sandbox

This project aims to provide a low barrier entry to trying rez - including optional
services like memcached and amqp - and getting a development and testing sandbox.

# Quickstart

## Windows

From the main repository folder:

```
.\scripts\build_image.ps1
docker compose up -d
.\scripts\set_rezconfig.ps1
