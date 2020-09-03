from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import CRUDapi
from .serializers import CRUDapiSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def student_list(request):
    # GET list of students, POST a new student, DELETE all students
	if request.method == 'GET':
		student = CRUDapi.objects.all()
		name = request.GET.get('name', None)
		
		if name is not None:
			students = student.filter(name__icontains=name)
      
			students_serializer = CRUDapiSerializer(students, many=True)
			return JsonResponse(students_serializer.data, safe=False)
		else:
			students_serializer = CRUDapiSerializer(student, many=True)
			return JsonResponse(students_serializer.data, safe=False)
		#return JsonResponse({'message': '400 Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)
 
	elif request.method == 'POST':
		student_data = JSONParser().parse(request)
		student_serializer = CRUDapiSerializer(data=student_data)
		
		if student_serializer.is_valid():
			student_serializer.save()
			return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED) 
		return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	else:
	#elif request.method == 'DELETE':
		student = CRUDapi.objects.all()
		student.delete()
		return JsonResponse({'message': 'Students were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def student_details(request, pk):
    # find student by pk (id)
	try: 
		student = CRUDapi.objects.get(pk=pk) 
	except CRUDapi.DoesNotExist: 
		return JsonResponse({'message': 'The student does not exist'}, status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'GET':
		students_serializer = CRUDapiSerializer(student)
		return JsonResponse(students_serializer.data)
	
	elif request.method == 'PUT': 
		student_data = JSONParser().parse(request) 
		student_serializer = CRUDapiSerializer(student, data=student_data) 
		if student_serializer.is_valid(): 
			student_serializer.save() 
			return JsonResponse(student_serializer.data) 
		return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	else:
		student.delete() 
		return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

		
        
@api_view(['GET'])
def student_gender(request):
    # GET all published students
	student = CRUDapi.objects.filter(gender=True)
        
	if request.method == 'GET': 
		students_serializer = CRUDapiSerializer(student, many=True)
		return JsonResponse(students_serializer.data, safe=False)