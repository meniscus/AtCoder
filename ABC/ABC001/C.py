from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

def get_wind_direction(deg) :
	if 11.25 <= deg and deg < 33.75 :
		return "NNE"
	elif 33.75 <= deg and deg < 56.25 :
		return "NE"
	elif 56.25 <= deg and deg < 78.75 :
		return "ENE"
	elif 78.75 <= deg and deg < 101.25 :
		return "E"
	elif 101.25 <= deg and deg < 123.75 :
		return "ESE"
	elif 123.75 <= deg and deg < 146.25 :
		return "SE"
	elif 146.25 <= deg and deg < 168.75 :
		return "SSE"
	elif 168.75 <= deg and deg < 191.25 :
		return "S"
	elif 191.25 <= deg and deg < 213.75 :
		return "SSW"
	elif 213.75 <= deg and deg < 236.25 :
		return "SW"
	elif 236.25 <= deg and deg < 258.75 :
		return "WSW"
	elif 258.75 <= deg and deg < 281.25 :
		return "W"
	elif 281.25 <= deg and deg < 303.75 :
		return "WNW"
	elif 303.75 <= deg and deg < 326.25 :
		return "NW"
	elif 326.25 <= deg and deg < 348.75 :
		return "NNW"
	else :
		return "N"
	


def get_wind_speed(wind_run) :
	return wind_run / 60.0

def get_wind_power(wind_speed) :
	wind_speed = float(Decimal(str(wind_speed)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
	
	if wind_speed <= 0.2 :
		return 0
	if wind_speed <= 1.5 :
		return 1
	if wind_speed <= 3.3 :
		return 2
	if wind_speed <= 5.4 :
		return 3
	if wind_speed <= 7.9 :
		return 4
	if wind_speed <= 10.7 :
		return 5
	if wind_speed <= 13.8 :
		return 6
	if wind_speed <= 17.1 :
		return 7
	if wind_speed <= 20.7 :
		return 8
	if wind_speed <= 24.4 :
		return 9
	if wind_speed <= 28.4 :
		return 10
	if wind_speed <= 32.6 :
		return 11
	
	return 12
		


args=input().split()
ans_deg = get_wind_direction(float(args[0]) / 10.0)

wind_speed = get_wind_speed(float(args[1]))

wind_power = get_wind_power(wind_speed)

if wind_power == 0 :
	ans_deg = "C"

print(str(ans_deg) + " " + str(wind_power))