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
```

# Contents

This project contains the following ready to use components. All services are
deployed as docker containers in a docker compose setup. A custom rezconfig.py
is provided to use with your existing rez setup. rez itself is currently NOT
part of the project.

> [!WARNING]
> Never use this in production. It is meant as a quick and easy way to get a
> a working test setup, nothing more.

## Caching with memcached

A standard memcached setup is provided and configured in the also included
rezconfig.py. You can inspect what exactly happens and if it works by setting
`REZ_DEBUG_MEMCACHE=1`

Caching includes directory traversals, package definitions, resolves for example.


## Context tracking with RabbitMQ, PostgreSQL and a basic consumer service

rez supports publishing resolve information to any AMQP compatible message queue.
RabbitMQ is used in this setup. To persist the published events a custom consumer
service is provided that stores the event data into the also included Postgres
database.

The current setup does not do a lot of normalization and stores the event data
as emitted by rez into a json column.

## pgadmin

A connected pgadmin instance is spun up to allow for easy inspection of the
data in the provided postgres instance

## Charting and analytics with metabase

Metabase is being deployed to allow for easy analytics and dashboards with the
data emitted and persisted.

> [!NOTE]
> Currently the connection to the postgres database needs to be setup manually
> in the GUI of metabase. This might be automated in the future, and if we can
> we will try to provide some sample charts and dashboards.

![(docs/images/metabase_01.png)]