from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status as Status

from validator.utils.validator import ValidatorUtirls
from validator.serializers.serializers import CPFSerializer

#from validate_docbr import CPF

class ValidatorCPF(APIView):
    def get(self, request, cpf):
        
        # Removi, pois alguns dos registros no arquivo não são válidos e estão retornando False.
        #doc_br_cpf = CPF()
        #doc_br_cpf.validate("000.000.000-99")
        if  len(cpf)  != 14:
            return JsonResponse({"error": "Verify length CPF"}, status=Status.HTTP_422_UNPROCESSABLE_ENTITY)

        status_cpf = {
            False: {"status": "FREE"},
            True: {"status": "BLOCK"}
        }
        free_or_block = ValidatorUtirls.verify_status_cpf(cpf) 
        #free_or_block = ValidatorUtirls.verify_status_cpf_with_pandas(cpf) 
        #data =  {"status": "BLOCK"} if free_or_block else {"status": "FREE"}
        serializer = CPFSerializer( data=status_cpf[free_or_block] )
        if not serializer.is_valid():
            data, status_code = ( serializer.errors, Status.HTTP_400_BAD_REQUEST  )
        else:
            data, status_code = ( serializer.data, Status.HTTP_200_OK )
        return JsonResponse(data, status=status_code)

    def put(self, request, cpf):
        pass

    def delete(self, request, cpf):
        pass
    
    def patch(self, request, cpf):
        pass

    def post(self, request, cpf):
        pass