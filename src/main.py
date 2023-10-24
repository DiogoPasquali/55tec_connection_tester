from connection.connection import Connection


if __name__ == '__main__':
    cn = Connection(
        user={
            'config_monitoring': {
                "connection": {
                    "active": True,
                    "ports": [80, 443, 22, 3306]
                }
            }
        },
    )

    cn.start()
