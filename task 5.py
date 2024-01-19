lugatlar = {
    'odam1': {'ism': 'John', 'byudjet': 5000},
    'odam2': {'ism': 'Jane', 'byudjet': 7000},
    'odam3': {'ism': 'Bob', 'byudjet': 6000}
}

yigindi = 0
for odam in lugatlar.values():
    yigindi += odam.get('byudjet', 0)

print(f"Odamalar byudjetlarining yig'indisi: {yigindi}")