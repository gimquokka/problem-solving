from collections import deque


def solution(record):
    answer = deque([])

    parse_record = deque([])
    nick_name = dict()

    for log in record:
        deque.append(parse_record, log.split(" "))
        if parse_record[-1][0] in ["Enter", "Change"]:
            nick_name[parse_record[-1][1]] = parse_record[-1][2]

    for parsed_log in parse_record:
        if parse_record[0] == "Change":
            continue
        elif parsed_log[0] == "Enter":
            final_name = nick_name[parsed_log[1]]
            answer.append("%s님이 들어왔습니다." % final_name)
        elif parsed_log[0] == "Leave":
            final_name = nick_name[parsed_log[1]]
            answer.append("%s님이 나갔습니다." % final_name)
    
    # print(list(answer))
    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
