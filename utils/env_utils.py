def readEnv(key):
    with open(f'.env', newline='') as env:
        for l in env.readlines():
            enviroment = l.split('=')
            if key in enviroment[0]:
                return enviroment[1]

