yosh = int(input("Yoshingizni kiriting: "))

if (yosh <= 4 and yosh > 0) or yosh >= 65:
    print("Chipta bepul.")
elif yosh >= 5 and yosh <= 12:
    print("Chipta narxi 15000 so'm.")
elif yosh >= 16 and yosh <= 64:
    print("Chipta narxi 20000 so'm.")
else:
    print("Yoshingizni noto'g'ri kiriydingiz!")



harorat = int(input("havo haroratini kiriting: "))

if harorat < 0:
    print("Havo juda sovuq!")
elif harorat >= 30:
    print("Havo juda issiq!")
elif harorat > 0 and harorat < 30:
    print("Havo harorati qulay.")



baho = int(input("Olgan bohoyingizni kiriting (0-100): "))

if baho > 90 and baho <= 100:
    print("A'lo!")
elif baho >= 80 and baho < 90:
    print("Yaxshi")
elif baho >= 70 and baho < 80:
    print("Qoniqarli")
elif baho < 70 and baho >= 1:
    print("Yomon")
else:
    print("Bunday baho mavjud emas!")