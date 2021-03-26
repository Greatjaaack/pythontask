def appearance(dict_session):
    '''
    :param arr: принимает словарь с сессими длительности урока, время нахождения ученика , время нахожденяи учителя
    :return: возвращает общее время нахождение ученика и учителя на уроке в секундах
    '''
    tutor = dict_session['tutor']
    pupil = dict_session['pupil']
    lesson = dict_session['lesson']
    result = []
    len_tutor = len(tutor)
    len_pupil = len(pupil)
    i = 0
    j = 0

    while i < len_tutor and j < len_pupil:

        while tutor[i+1] < pupil[j]:
            i += 2
        while pupil[j+1] < tutor[i]:
            j += 2

        if tutor[i] >= pupil[j]:
            if len(result) >= 1:
                if tutor[i] < end:
                    start = end
                else:
                    start = tutor[i]
            else:
                start = tutor[i]
        else:
            if len(result) >= 1:
                if pupil[j] < end:
                    start = end
                else:
                    start = pupil[j]
            else:
                start = pupil[j]

        if lesson[0] > start:
            start = lesson[0]

        if pupil[j + 1] <= tutor[i + 1]:
            end = pupil[j + 1]
            j += 2
        else:
            end = tutor[i + 1]
            i += 2

        if lesson[1] < end:
            end = lesson[1]
            result.append([start, end])
            break

        if lesson[0] > start:
            start = lesson[0]

        if start <= end:
            result.append([start, end])

    def total_time(result):
        '''
        :param result: принимает список вида list [[start_time,end_time],--//--]
        :return: возвращает общее время нахождение ученика и учителя на уроке в секундах
        '''
        total = 0
        for i in result:
            total += i[1] - i[0]
        return total

    return total_time(result)


tests = [
   {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    'answer': 3117
    },
   {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'