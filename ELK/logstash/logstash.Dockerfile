ARG ELK_VERSION

# https://www.docker.elastic.co/
FROM docker.elastic.co/logstash/logstash:${ELK_VERSION}

# 여기에 플러그인 추가
# Example: RUN logstash-plugin install logstash-filter-json