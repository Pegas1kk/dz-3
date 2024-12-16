users = {}
while True:
    name = input("Имя: ")
    if not name: break
    surname = input("Фамилия: ")
    if not surname: break
    age_str = input("Возраст: ")
    if not age_str.isdigit() or not 18 <= int(age_str) <= 60: break
    user_id = input("ID: ").zfill(8) #очень удобная штука
    if not user_id: break
    if not name.isalpha() or not surname.isalpha():
        print("Имя и фамилия должны состоять из букв.")
        continue
    if user_id in users:
        print("ID уже существует.")
        continue

    users[user_id] = (name.capitalize(), surname.capitalize(), int(age_str))

title = ["ID", "Имя", "Фамилия", "Возраст"]
widths = [max(len(str(item)), len(h)) for h, item in zip(title, [users.keys()] + [list(x) for x in zip(*users.values())])]
print(" ".join(h.ljust(w) for h, w in zip(title, widths)))
print("-" * sum(widths) + "-")
for id, (name, surname, age) in users.items():
    print(f"{id:<{widths[0]}} {name:<{widths[1]}} {surname:<{widths[2]}} {age:<{widths[3]}}")
# боль