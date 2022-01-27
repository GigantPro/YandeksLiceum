ls = {}
 
 
def get_transactions(t: str):
    if t == "print_it":
        for x, info in ls.items():
            print(f"{info['count']} {x} {info['summa']}")
        return
    card_num, t, amount = t.replace("-", " ").replace(":", " ").split()
    result = ls.get(t, {"count": 0, "summa": 0})
    result["count"] += 1
    result["summa"] += int(amount)
    ls[t] = result