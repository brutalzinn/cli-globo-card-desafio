def read_env(key):
    print("Lendo configurações do arquivo .env")
    with open(f'.env', newline='') as env:
        for l in env.readlines():
            enviroment = l.split('=')
            if key in enviroment[0]:
                return enviroment[1]

