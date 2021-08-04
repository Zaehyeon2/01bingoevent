from bs4 import BeautifulSoup
import requests

print("""
████████╗██╗  ██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗  ██████╗ ██████╗ 
╚══██╔══╝██║  ██║██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ ██╔═══██╗██╔══██╗
   ██║   ███████║█████╗  █████╔╝ ██║██╔██╗ ██║██║  ███╗██║   ██║██║  ██║
   ██║   ██╔══██║██╔══╝  ██╔═██╗ ██║██║╚██╗██║██║   ██║██║   ██║██║  ██║
   ██║   ██║  ██║███████╗██║  ██╗██║██║ ╚████║╚██████╔╝╚██████╔╝██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═════╝ 
                                                                        
                                                                        """)

print("영과일 백준 빙고 이벤트")

nickname = input("\n백준 닉네임을 입력하세요: ")

url = "https://www.acmicpc.net/user/{}".format(nickname)

html = requests.get(url)

if (html.status_code == 404) :
    input("백준에서 해당 닉네임을 찾을 수 없습니다. 엔터키를 누르면 종료됩니다.")
else :
    bingo = [[17451, 18240, 16493, 15681, 15725],
            [1655, 14924, 15734, 17419, 17449],
            [1874, 2444, 20436, 16396, 18242], 
            [17215, 21867, 18238, 16430, 19542],
            [18111, 17178, 1697, 18244, 17213]]

    result = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

    bingo_list = []

    bingo5x5 = 0
    bingo3x3 = 0

    html = html.text
    soup = BeautifulSoup(html, 'html.parser')
    problems = soup.select("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.col-md-9 > div:nth-child(1) > div.panel-body > a")
    
    problem_num_list = []
    for x in problems:
        problem_num_list.append(int(x.get_text()))
    
    print("\n\"{}\"님의 빙고 리스트\n".format(nickname))

    for i in range(5):
        for j in range(5):
            if bingo[i][j] in problem_num_list:
                result[i][j] = 1
                print("■", end="")
                bingo_list.append(bingo[i][j])
            else :
                print("□", end="")
        print()
    
    print()

    for i in range(5):
        if (result[0][i] and result[1][i] and result[2][i] and result[3][i] and result[4][i]): bingo5x5 += 1
        if (result[i][0] and result[i][1] and result[i][2] and result[i][3] and result[4][i]): bingo5x5 += 1
    if (result[0][0] and result[1][1] and result[2][2] and result[3][3] and result[4][4]): bingo5x5 += 1
    if (result[0][4] and result[1][3] and result[2][2] and result[3][1] and result[4][1]): bingo5x5 += 1

    for i in range(3):
        if (result[1][i+1] and result[2][i+1] and result[3][i+1]): bingo3x3 += 1
        if (result[i+1][1] and result[i+1][2] and result[i+1][3]): bingo3x3 += 1
    if (result[1][1] and result[2][2] and result[3][3]): bingo3x3 += 1
    if (result[1][3] and result[2][2] and result[3][1]): bingo3x3 += 1

    print("5x5 빙고 개수: {}개".format(bingo5x5))
    print("3x3 빙고 개수: {}개".format(bingo3x3))
    print()

    input("엔터키를 누르면 종료됩니다.")