# Создание потоков
import threading
import time

def write_words(word_count: int, file_name: str):
    with open(file_name, 'w') as file:
        for s in range(word_count):
            file.write(f'Какое-то слово № {s + 1}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

args = (10, 30, 200, 100)

start = time.time()
for k in range(len(args)):
    write_words(args[k], f'example{k + 1}.txt')
stop = time.time()
print(f'Работа потоков {stop - start} c')

start = time.time()
threads = {f'thread_{i + 1}': threading.Thread(target=write_words, args=(args[i], f'example{i + 5}.txt')) for i in range(4)}
for _, v in threads.items():
    v.start()
for _, v in threads.items():
    v.join()
stop = time.time()
print(f'Работа потоков {stop - start} c')

