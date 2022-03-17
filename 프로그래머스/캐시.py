def solution(cacheSize, cities):
    cache = []
    time = 0

    for city in cities:
        # 소문자 변환
        city = city.lower()
        # 만약 cachesize가 0이면 모두 cache miss이므로 도시이름별 +5
        if cacheSize == 0:
            time += 5
        # cachesize가 0이 아닌 경우
        else:
            # cache hit
            # city가 cache안에 있을 때 기존의 city제거 후 새로 추가
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
            
            # cache miss
            # city가 cache안에 없을 때
            else:
                # cache가 이미 꽉 차있다면 제일 앞에꺼 제거후 새로 추가 
                if len(cache) == cacheSize:
                    cache.pop(0)
                    cache.append(city)
                    time += 5
                # 꽉 차있지 않다면 그냥 추가
                else:
                    cache.append(city)
                    time += 5
                
    return time