import random
import time
import threading

def ask_question(a, b):
    correct_answer = a * b
    attempts = 0
    answer = None

    def timed_input():
        nonlocal answer
        answer = input(f"{a} ✕ {b} = ")

    while attempts < 3:
        answer = None
        input_thread = threading.Thread(target=timed_input)
        input_thread.start()
        input_thread.join(timeout=8)

        if answer is None:
            print("時間切れ！")
            attempts += 1
        else:
            try:
                if int(answer) == correct_answer:
                    print("正解！")
                    time.sleep(1)
                    return True
                else:
                    print("不正解！")
                    attempts += 1
            except ValueError:
                print("無効な入力です。整数を入力してください。")
                attempts += 1

    print(f"正解は {correct_answer} でした。")
    return False

def multiplication_quiz():
    score = 0
    for question_number in range(10):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        if ask_question(a, b):
            score += 1

    print(f'得点: {score} / 10')

if __name__ == "__main__":
    multiplication_quiz()

