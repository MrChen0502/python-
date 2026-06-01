def uName(a,b,**map):
    print(f"a:{a},b:{b},map:{map}")
    for k,v in map.items():
        print(f"k:{k},v:{v}")

print(uName(1,2,name="mayikt",age=22,address="湖北武汉"))