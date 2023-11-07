from connection.connection import Connection


if __name__ == '__main__':
    cn = Connection(
        user={
            'config_monitoring': {
                "connection": {
                    "active": True,
                    "ports": []
                }
            }
        },
        path="C:\\55pbx"
    )

    cn.start()
