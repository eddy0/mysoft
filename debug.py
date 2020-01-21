from app import configured_app

if __name__ == '__main__':
    a = configured_app()
    a.run(
        debug=True,
        host='localhost',
        port=3000,
    )
