#[?] 원본 데이터 중에서 대상 데이터와 가장 가까운 값

# 근삿값 알고리즘(Near Algorithm) : 가까운 값 -> 차잇값의 절댓값의 최솟값
def main():
    #[0] Initialize
    min = 99999 # 차잇값의 절댓값의 최솟값이 담길 그릇

    #[1] Input
    numbers = [ 10, 20, 30, 27, 17]
    target = 25 # target과 가까운 값
    near = 0 # 가까운 값 : 27

    #[2] Process

    #[3] Output
    print(f'{target}와/과 가장 가까운 값 : {near}(차이 : {min})')

if __name__ == '__main__':
  main()