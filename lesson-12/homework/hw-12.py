# Exercise 1: Threaded Prime Number Checker
import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    result.extend(primes)

if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4
    threads = []
    result = []

    chunk_size = (end_range - start_range) // num_threads

    for i in range(num_threads):
        start = start_range + i * chunk_size
        end = start_range + (i + 1) * chunk_size if i != num_threads - 1 else end_range
        thread = threading.Thread(target=check_primes, args=(start, end, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Primes found:", sorted(result))

# Exercise 2: Threaded File Processing
import threading
from collections import defaultdict

def count_words(lines, word_counts_lock, word_counts):
    local_counts = defaultdict(int)
    for line in lines:
        for word in line.strip().split():
            word = word.lower().strip('.,!?()[]{}:;"\'')
            local_counts[word] += 1
    with word_counts_lock:
        for word, count in local_counts.items():
            word_counts[word] += count

if __name__ == "__main__":
    file_path = "salt.txt" 
    num_threads = 4

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    word_counts = defaultdict(int)
    word_counts_lock = threading.Lock()

    for i in range(num_threads):
        chunk = lines[i * chunk_size : (i + 1) * chunk_size if i != num_threads - 1 else len(lines)]
        thread = threading.Thread(target=count_words, args=(chunk, word_counts_lock, word_counts))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{word}: {count}")
