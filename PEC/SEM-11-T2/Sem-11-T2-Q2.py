def fibo(n, a=0, b=1, count=1, seq='0, 1'):
    count += 1
    if count == n:
        return seq
    else:
        c = b + a
        seq += f', {c}'
        return fibo(n, b, c, count, seq)


def main():
    print(fibo(int(input())))


if __name__ == '__main__':
    main()