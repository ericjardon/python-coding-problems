def switchCase(command, a, b):
    return {
        '+': lambda: a + b,
        '-': lambda: a - b,
        '*': lambda: a * b,
        '/': lambda: a / b,
    }.get(command, lambda: None)()

# switch case returns an anonymous function corresponding to the given command.
# the default is a lambda returnirn None, in case the command is not recognized.

def interpret(value, commands, args):
    ans = value

    for i in range(len(commands)):
        ans = switchCase(commands[i], ans, args[i])
        if ans == None:
            return -1

    return ans

test = []
test.append(interpret(1, ['+'], [1]))
test.append(interpret(1, ['+', '*'], [1, 3]))
print(test)