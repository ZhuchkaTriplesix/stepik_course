def main():
    n = int(input().strip())
    submissions = [input().strip() for _ in range(n)]

    correct_students = set()
    total_attempts = len(submissions)
    correct_attempts = 0

    for submission in submissions:
        nickname, result = submission.split(': ')
        if result == 'Correct':
            correct_students.add(nickname)
            correct_attempts += 1
        elif result == 'Wrong':
            continue

    unique_correct_count = len(correct_students)

    if unique_correct_count > 0:
        correct_percentage = round((correct_attempts / total_attempts) * 100)
        print(f"Верно решили {unique_correct_count} учащихся")
        print(f"Из всех попыток {correct_percentage}% верных")
    else:
        print("Вы можете стать первым, кто решит эту задачу")


main()
