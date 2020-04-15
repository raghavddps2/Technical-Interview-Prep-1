if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    winner_score = max(arr)
    runner_score = 0
    for i in arr:
        print(i)
        if i < winner_score and i > runner_score:
            print("hi")
            runner_score = i
    print(runner_score)
