if __name__ == '__main__':
    import sys
    while True:
        line = sys.stdin.readline().rstrip()
        if line == 'END':
            break
        reversed_str = "".join(reversed(line))
        print(reversed_str)
