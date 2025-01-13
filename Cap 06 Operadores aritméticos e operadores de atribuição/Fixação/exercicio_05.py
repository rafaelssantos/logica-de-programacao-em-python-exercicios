# Os valores estão fixos, para usar valores que possam ser modificados 
# pelo usuário é necessário usar a função input().
total_em_segundos = 500000
dias = total_em_segundos // 86400
resto_dias = total_em_segundos % 86400
horas = resto_dias // 3600
resto_horas = resto_dias % 3600
minutos = resto_horas // 60
segundos = resto_horas % 60

print(dias, "dia(s) ", horas, "hora(s) ", minutos, "minuto(s) e ", segundos, "segundo(s).")