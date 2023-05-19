import random
import sys

random_version = random.getstate()[0]
print("PYTHON_VERSION:" + str(sys.version))
print("RANDOM_VERSION:" + str(random_version))

# PINの桁数を定数化している
PIN_DIGIT = 32
TEST_PIN_DIGIT = 6
# Unicodeの範囲の最小と最大を定数化している
PIN_MIN = 48
PIN_MAX = 122

# ランダムな数字のリストを文字化する関数
def unicode(num_list: list[int], test = False) -> str:
    # テスト用
    if test == True:
        unicoded = [0] * TEST_PIN_DIGIT
        for i in range(TEST_PIN_DIGIT):
            unicoded[i] = chr(num_list[i])
        return "".join(unicoded)
    
    # Unicode化する
    unicoded = [0] * PIN_DIGIT
    for i in range(PIN_DIGIT):
        unicoded[i] = chr(num_list[i])
    return "".join(unicoded)

# ランダムな数字を生成する関数
def generate_random_numbers(test = False) -> list[int]:
    # テスト用
    if test == True:
        return [48, 57, 65, 90, 97, 122] # "09AZaz"の10進数表記で返される

    num_list = list()
    for _ in range(PIN_DIGIT):
        while True:
            # 数字の範囲はUnicode表を参照して、指定する
            num = random().randint(PIN_MIN, PIN_MAX)
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