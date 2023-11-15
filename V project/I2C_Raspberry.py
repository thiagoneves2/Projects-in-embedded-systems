import smbus
import time
#Define o endereço como 8
address  = 8

#Inicializa o barramento
bus = smbus.SMBus(1)

while True:
	#Faz uma requisição de leitura de dados por bloco (Já que foram 2 bytes enviados)
	data = bus.read_i2c_block_data(address, 0, 2)
	#junta-se os valores dos dois bytes
	potVal = data[0]*256 + data[1]
	print(potVal)
	time.sleep(0.5)

