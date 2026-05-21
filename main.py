# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def process_grades(list_of_grades, double = False):
    '''
    Если вывод предполагает наличие дубликатов установить double = True
    '''
    answer = {'valid_count': 0, 'average': 0.0, 'passed': [], 'skipped': 0}
    for record in list_of_grades:
        record = record.split(':')
        try:
            grade = int(record[1])
            student = record[0]
            student[1].lower() # В качестве длинны самой короткой фамилии выбрал 2
            answer['average'] = (answer['average'] * answer['valid_count'] + grade) / (answer['valid_count'] + 1)
            answer['valid_count'] += 1
            if grade >= 60:
                answer['passed'].append(student)
        except ValueError:
            answer['skipped'] += 1
        except IndexError:
            answer['skipped'] += 1
    if double:
        print(answer['passed'])
        answer['passed'] = set(answer['passed'])
    return answer

list = ['GSDGg:65','ewfwfw:sdfs',':70','er:80', 'er:70']

print(process_grades(list,True))
print(process_grades(list))


