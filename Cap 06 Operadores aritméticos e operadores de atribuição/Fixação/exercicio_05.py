# Os valores estão fixos, para usar valores que possam ser modificados pelo usuário 
# é necessário usar a função input().

total_em_segundos = 500000
dias = total_em_segundos // 86400           # 1 dia tem 86400 segundos
resto_dias = total_em_segundos % 86400      # Separando o resto de segundos do dia
horas = resto_dias // 3600                  # 1 hora tem 3600 segundos
resto_horas = resto_dias % 3600             # Separando o resto de segundos da hora
minutos = resto_horas // 60                 # 1 minuto tem 60 segundos 
segundos = resto_horas % 60                 # Resto do segundo

print(dias, "dia(s) ", horas, "hora(s) ", minutos, "minuto(s) e ", segundos, "segundo(s).")