from openpyxl import load_workbook

wb = load_workbook(filename="../resources/Heavy Lift Plan and Delivery Schedule-3.xlsx")

ws = wb["Dress up Items _20200711"]

results = []
for value in list(ws.values)[6:24]:
    results.append(list((value[0], value[1], value[3], value[4], value[5])))

# print(json.dumps(results, default=str))
for row in results:
    print(row)
