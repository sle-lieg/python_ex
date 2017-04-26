if __name__ == '__main__':
    N, i = int(input()), 0
    lis = []
    cmd = []
    while i < N:
        s = input()
        cmd = s.split()
        print(cmd[0])
        if cmd[0] == "print":
            print(lis)
        elif cmd[0] == "insert":
            lis.insert(int(cmd[1]), cmd[2])
        elif cmd[0] == "remove":
            lis.remove(cmd[1])
        elif cmd[0] == "append":
            lis.append(cmd[1])
        elif cmd[0] == "sort":
            lis.sort()
        elif cmd[0] == "pop":
            lis.pop()
        elif cmd[0] == "reverse":
            lis.reverse()
        i += 1