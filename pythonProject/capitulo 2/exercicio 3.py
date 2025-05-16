print("tempo do primeiro trecho")
minutoPrimeiroTrecho = 8 * 40
segundoprimeirotrecho = 15
print("tempo do primeiro trecho se segundos: ", totalTempoPrimeirotrecho)

print("tempo do segundo trecho: 7min e 12seg")
minutosSegundoTrecho = (7 * 3) * 60
segundosSegundoTrecho = 12
print("tempo de segundo trecho em segundos: ", totalTempoSegundoTrecho)

print("Tempo do terceiro trecho: 8 min e 15 s")
minutoTerceiroTrecho = 8 * 60
segundoTerceiroTrecho = 15
print("Tempo do terceiro trecho em segundo ", totalTempoTerceiroTrecho)

#soma o total de elementos e coverte os todos os segundos em minutos
totalTempoTodosTrechosMnutos = (totalTempoPrimeiroTrecho + totalTempoSegundoTrecho + totalTempoTerceiroTrecho)
#Soma valor total dos segundos
totalTempoTodosTrechosSegundos = (totalTempoPrimeiroTrecho + totalTempoSegundoTrecho + segundoTerceiroTrecho / 60)

restanteMinutos: int(totalTempoTodosTrechosSegundos / 60)
restanteSegundos: totalTempoTodosTrechosSegundos % 60

totalMinutos = totalTempoTodosTrechosMnutos + restanteMinutos
totalSegundos = restanteSegundos

print("soma de tempo de todos os trechos: ", totalTempoTodosTrechosMnutos, "minutos")
print("soma de tempo de todos os trecho: ", totalTempoTodosTrechosSegundos

horasInicial = (6 * 60) * 60
minutoInicialSegundos = 52 * 60
horasInicialSegundos = horasInicialSegundos + minutoInicialSegundos
totalTrechoMinutosSegundos = totalMinutos * 60

horaChegada = int(((horasInicialSegundos + TempoTrechosMnutosSegundos) / 60) /60 )
minutochegada = int(((minutosInicialSegundos + tempoTrechosMinutosSegundos) /60) % 60 )
print("O tempo de chegada foi de ", horaChegada, ":", minutochegada, restanteSegundos)