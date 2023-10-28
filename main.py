import random

def get_user_choice():
    user_choice = input("Taş?, Kağıt?, Makas?: ").lower()
    while user_choice not in ["taş", "kağıt", "makas"]:
        user_choice = input("Lütfen geçerli bir seçenek giriniz --> (Taş?, Kağıt?, Makas?): ").lower()
    return user_choice

def get_comp_choice():
    choices = ["taş", "kağıt", "makas"]
    comp_choice = random.choice(choices)
    return comp_choice

def match_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Berabere"
    elif ((user_choice == "taş" and comp_choice == "makas")
          or (user_choice == "makas" and comp_choice == "kağıt")
            or (user_choice == "kağıt" and comp_choice == "taş")):
        return "Kazandınız"
    else:
        return "Bilgisayar kazandı"

def play():
    user_choice = get_user_choice()
    comp_choice = get_comp_choice()
    print(f"Sizin tercihiniz: {user_choice}")
    print(f"Bilgisayarın tercihi: {comp_choice}")
    result = match_winner(user_choice,comp_choice)
    print(result)

if __name__ == "__main__":
    print("Taş Kağıt Makas Oyununa Hoşgeldiniz!")
    while True:
        play()
        play_again = input("Tekrar oynamak isterseniz 'e', istemezseniz 'h' tuşuna basın!: ")
        if play_again == "h":
            print("Oynadığınız için teşekkürler!")
            break