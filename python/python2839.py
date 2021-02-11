#사탕가게에 설탕을 N킬로그램 배달
#설탕공장에서 만드는 설텅은 봉지에
#3킬로그램봉지, 5킬로그램 봉지
#최소한의 봉지만 쓸때
#정확하게 N킬로그램 만들수 없으면 -1
a = 11
bascket = 0

while a >= 0:
    if(a%5) == 0:
        bascket += a//5
        print(bascket)
        break
    a -= 3
    bascket += 1
else:
    print(-1)
