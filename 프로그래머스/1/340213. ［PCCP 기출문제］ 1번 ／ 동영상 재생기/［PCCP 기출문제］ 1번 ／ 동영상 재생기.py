def solution(video_len, pos, op_start, op_end, commands):
    # 시간을 다 초로 변환
    video_len = (int(video_len[0:2]) * 60) + int(video_len[3:5])
    pos = (int(pos[0:2]) * 60) + int(pos[3:5])
    op_start = (int(op_start[0:2]) * 60) + int(op_start[3:5])
    op_end = (int(op_end[0:2]) * 60) + int(op_end[3:5])
    
    
    for i in commands:
        if pos <= op_end and pos >= op_start:
            pos = op_end
        
        if i == "prev":
            if pos - 10 <= 0:
                pos = 0
            else:
                pos -= 10
        
        elif i == "next":
            if pos + 10 >= video_len:
                pos = video_len
            else:
                pos += 10
    
    if pos <= op_end and pos >= op_start:
            pos = op_end
            
    h = pos // 60
    m = pos % 60
    answer = ''
    if h <= 10:
        answer += '0'+str(h)
    else:
        answer += str(h)
    answer += ':'

    if m <= 10:
        answer += '0'+str(m)
    else:
        answer += str(m)
        
    return answer