import random
logo=r'''

.____                                  ________            ___ ___ .__       .__
|    |    ______  _  __ ___________    \_____  \_______   /   |   \|__| ____ |  |__   ___________
|    |   /  _ \ \/ \/ // __ \_  __ \    /   |   \_  __ \ /    ~    \  |/ ___\|  |  \_/ __ \_  __ \
|    |__(  <_> )     /\  ___/|  | \/   /    |    \  | \/ \    Y    /  / /_/  >   Y  \  ___/|  | \/
|_______ \____/ \/\_/  \___  >__|      \_______  /__|     \___|_  /|__\___  /|___|  /\___  >__|
        \/                 \/                  \/               \/   /_____/      \/     \/


'''
print(logo)
celebrities = [
    {
        "name": "Cristiano Ronaldo",
        "followers_count": 599,  # 599M
        "description": "Professional footballer, plays for Al-Nassr and Portugal",
        "country": "Portugal"
    },
    {
        "name": "Lionel Messi",
        "followers_count": 484,  # 484M
        "description": "Professional footballer, plays for Inter Miami and Argentina",
        "country": "Argentina"
    },
    {
        "name": "Selena Gomez",
        "followers_count": 430,  # 430M
        "description": "Singer, actress, and producer",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "followers_count": 400,  # 400M
        "description": "Model, businesswoman, and reality TV star",
        "country": "United States"
    },
    {
        "name": "Dwayne 'The Rock' Johnson",
        "followers_count": 393,  # 393M
        "description": "Actor, producer, and former professional wrestler",
        "country": "United States"
    },
    {
        "name": "Ariana Grande",
        "followers_count": 392,  # 392M
        "description": "Singer, songwriter, and actress",
        "country": "United States"
    },
    {
        "name": "Kim Kardashian",
        "followers_count": 366,  # 366M
        "description": "Media personality, businesswoman, and reality TV star",
        "country": "United States"
    },
    {
        "name": "Beyoncé",
        "followers_count": 318,  # 318M
        "description": "Singer, songwriter, actress, and businesswoman",
        "country": "United States"
    },
    {
        "name": "Justin Bieber",
        "followers_count": 291,  # 291M
        "description": "Singer, songwriter, and musician",
        "country": "Canada"
    },
    {
        "name": "Taylor Swift",
        "followers_count": 269,  # 269M
        "description": "Singer-songwriter and music producer",
        "country": "United States"
    },
    {
        "name": "Khloé Kardashian",
        "followers_count": 313,  # 313M
        "description": "Media personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Neymar Jr.",
        "followers_count": 213,  # 213M
        "description": "Professional footballer, plays for Al-Hilal and Brazil",
        "country": "Brazil"
    },
    {
        "name": "Jennifer Lopez",
        "followers_count": 253,  # 253M
        "description": "Singer, actress, and businesswoman",
        "country": "United States"
    },
    {
        "name": "Virat Kohli",
        "followers_count": 256,  # 256M
        "description": "Professional cricketer, plays for India",
        "country": "India"
    },
    {
        "name": "Kendall Jenner",
        "followers_count": 313,  # 313M
        "description": "Model and media personality",
        "country": "United States"
    },
    {
        "name": "Nicki Minaj",
        "followers_count": 224,  # 224M
        "description": "Rapper, singer, and songwriter",
        "country": "Trinidad and Tobago"
    },
    {
        "name": "Miley Cyrus",
        "followers_count": 213,  # 213M
        "description": "Singer, songwriter, and actress",
        "country": "United States"
    }
]

def find_score():


    digit = random.randint(1, len(celebrities)-1)
    score=0
    is_true=True
    while is_true:
        print(f"Compare A: {celebrities[digit]["name"]} , {celebrities[digit]["description"]} ,  {celebrities[digit]["country"]}")

        vs=r'''

    ____   _____________
    \   \ /   /   _____/
     \   Y   /\_____  \
      \     / /        \
       \___/ /_______  /
                     \/

           '''
        print(vs)

        digit2=random.randint(1,len(celebrities)-1)
        print(f"Compare B: {celebrities[digit2]["name"]} , {celebrities[digit2]["description"]} ,  {celebrities[digit2]["country"]}")
        if digit==digit2:
            print(f"You can select A to continue,The value is same")
            print

        answer=input("Who has more followers : A or B ? ").upper()
        followers_A=celebrities[digit]["followers_count"]
        followers_B = celebrities[digit2]["followers_count"]
        A=followers_A
        B=followers_B
        greater=max(followers_A,followers_B)
        if greater== A:
            winner="A"
        else:
            winner="B"
        if str(answer) == str(winner):
            score+=1
            print(f"You are right ! . Current score ={score} ")
            if winner=="B":
                digit=digit2

        else:
            is_true=False
            print(f"Sorry ,that's wrong . Final score = {score}")

find_score()
