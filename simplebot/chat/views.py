from django.shortcuts import render

# Create your views here.


input_data=input('enter your msg: ----- ')

greet=['hi','Hi','HI','Hello','HELLO','hello']

howu=['How are you','how are you','how r u']

def get_response(request):
	msg=input_data
	if msg in greet:
		hi='bot:Hi there..!! '
		#return hi
		print(hi)
	elif msg in howu:
		fine='bot:Fine'
		#return fine
		print(fine)
	elif msg == 'bye':
		break;
	else:
		sorry='bot:sorry yar we dint find '
		print(sorry)
