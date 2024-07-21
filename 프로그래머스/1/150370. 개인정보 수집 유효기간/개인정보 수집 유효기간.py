def date2day(date):
    # 날짜를 일 수로 바꾸는 코드
    # 1년 = 12 * 28
    total_days = 0
    y, m, d = map(int, date.split('.'))
    total_days += y * 12 * 28
    total_days += m * 28
    total_days += d
    return total_days
    
def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    for term in terms:
        type_, validation_month = term.split()
        terms_dict[type_] = int(validation_month) * 28
        
    for idx, privacy in enumerate(privacies):
        created_date, type_ = privacy.split()
        
        remained_day = date2day(today) - date2day(created_date)
        if remained_day >= terms_dict[type_]:
            answer.append(idx + 1)
            
    return answer