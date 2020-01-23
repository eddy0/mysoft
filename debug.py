from app import configured_app

if __name__ == '__main__':
    a = configured_app()
    a.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
    )
