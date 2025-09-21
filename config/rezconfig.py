memcached_uri = ["127.0.0.1:11211"]

context_tracking_host = "127.0.0.1"

context_tracking_amqp = {
    "userid": "rabbitmq",
    "password": "rabbitmq",
    "connect_timeout": 5,
    "exchange_name": "rez",
    "exchange_routing_key": "REZ.CONTEXT",
    "message_delivery_mode": 1,
}