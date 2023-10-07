def solution(participant, completion):
    from collections import Counter
    participant = dict(Counter(participant))
    completion = dict(Counter(completion))
    for i in participant :
        if i not in completion or participant[i] > completion[i] :
            return i