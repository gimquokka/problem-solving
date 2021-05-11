def solution(record):
    answer = []
    namespace = dict()
    printer = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    
    for log in record:
        parsed_log = log.split(" ")
        if parsed_log[0] != "Leave":
            namespace[parsed_log[1]] = parsed_log[2]
    
    for log in record:
        parsed_log = log.split(" ")
        if parsed_log[0] != "Change":
            # print(namespace[parsed_log[1]] + printer[parsed_log[0]])
            answer.append(namespace[parsed_log[1]] + printer[parsed_log[0]])
    
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])