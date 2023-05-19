import random
import sys

random_version = random.getstate()[0]
print("PYTHON_VERSION:" + str(sys.version))
print("RANDOM_VERSION:" + str(random_version))

# PINの桁数を定数化している
PIN_DIGIT = 32

# ランダムな数字のリストを文字化する関数
def unicode(num_list: list[int]) -> str:
    # Unicode化する
    unicoded = [0] * PIN_DIGIT
    for i in range(PIN_DIGIT):
        unicoded[i] = chr(num_list[i])
    return unicoded

# ランダムな数字を生成する関数
def generate_random_numbers() -> list[int]:
    num_list = list()
    for _ in range(PIN_DIGIT):
        while True:
            # 数字の範囲はUnicode表を参照して、指定する
            num = random.randint(48, 122)
            # 記号のUnicodeが出てきた場合、再び数字を生成する処理
            if not ((58 <= num <= 64) or (91 <= num <= 96)):
                num_list.append(num)
                break
    return num_list

# PINコードを発行する関数(main関数)
def main() -> str:
    random_list = generate_random_numbers()
    PIN = unicode(random_list)
    print("".join(PIN))
    return PIN

if __name__ == '__main__':
    main()