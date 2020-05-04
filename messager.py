import random

def check(ctx):
    print(ctx)
    if ('ok marc') in ctx:
        msg = 'ok marc'
        return msg
    
    if ('bet') in ctx.split():
        filename = './quips/betlist.txt'
        with open(filename, 'r') as file:
            data = file.readlines()
        msg = "I'll bet " + str(random.choice(data))
        flag = False
        return msg, flag
    
    if ('good bot' in ctx)  or ('bad bot' in ctx):
        filename = "longtermdata.txt"
        with open(filename, 'r') as file:
            data = file.readlines()
        if ('bad bot') in ctx:
            data[1] = str(int(data[1]) - 1) + '\n'
            msg = ':rage: You :rage: brought :rage: my :rage: thanks :rage: to :rage: ' + data[1].strip('\n') + 'th :rage: hope :rage: you :rage: feel :rage: good :rage:'
        if ('good bot') in ctx:
            data[1] = str(int(data[1]) + 1) + '\n'
            msg = 'Thank :clap: you :clap: are :clap: the :clap: ' + data[1].strip('\n') + 'th :clap: person :clap: to :clap: thank :clap: me. :clap:'
        with open(filename , 'w') as file:
            file.writelines(data)
        flag = True
        return msg, flag
    
    if ('f') in ctx.split():
        msg = 'F'
        flag = False
        return msg, flag

    if ('http') in ctx:
        msg = 'nice'
        flag = False
        return msg, flag

    if ('flumbot' in ctx):
        filename = './quips/botlist.txt'
        with open(filename, 'r') as file:
            data = file.readlines()
        msg = str(random.choice(data))
        flag = False
        return msg, flag

    if ('bible' in ctx):
        msg = 'To glorify God by being a faithful steward of all that is entrusted to us and to have a positive influence on all who come in contact with Chick-fil-A.'
        flag = False
        return msg, flag

    msg = 'oop'
    flag = False
    return msg, flag

        
        
        
