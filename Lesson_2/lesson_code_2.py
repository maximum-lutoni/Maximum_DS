hour = 17

if hour > 12:
    print("День")
elif hour > 16:
    print("Вечер")

hour = int(input())

if hour > 12 and hour <= 16:
    print("День")
elif hour > 16 and hour <= 23:
    print("Вечер")
elif hour > 23 or hour <= 3:
    print("Ночь")
elif hour > 3 and hour <= 12:
    print("Утро")

a, b, c = 12,13,14
max_var = max(a,b,c)
min_var = min(a,b,c)