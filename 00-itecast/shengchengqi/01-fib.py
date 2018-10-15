
def fib():
    a, b = 0, 1
    for x in range(5):
        yield b
        a, b = b, a + b

r = fib()
print(r) #<function fib at 0x00884228> 可以看到结果是生成器

print(next(r)) # 通过next()函数可以打印出结果
print(next(r))
print(next(r))
print(next(r))
print(next(r))

print("-----------------")
for x in r:
    print(x)


