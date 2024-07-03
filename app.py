def solution(N):
    import string
    alphabet = string.ascii_lowercase 

    k = min(26, N)

    q = N // k
    r = N % k

    result = (alphabet[:k] * q) + alphabet[:r]

    return result

# Examples
print(solution(10))
print(solution(7))
print(solution(40)) 