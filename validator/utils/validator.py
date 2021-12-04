import pandas as pd

class ValidatorUtirls():

    @staticmethod
    def verify_status_cpf(cpf: str) -> bool:
        """[Função responsável por verificar o status do cpf]
        Args:
            cpf (str): [String com 14 caracteres]
        Returns:
            bool: [Retorna True se o cpf estiver no arquivo e False se não estiver.]
        """
        #Removi, pois no end-point que chama essa função já existe uma validação voltada para isso.
        #if not isinstance(cpf, str)  or  len(cpf)  != 14:
        #    raise Exception("CPF invalid")
        free_or_block = False
        archive = open("./blacklist.txt",  encoding='utf-8', errors='ignore')
        list_cpf = [ cpf_in_archive.strip()  for cpf_in_archive in archive.readlines() if cpf == cpf_in_archive.strip() ]
        free_or_block = bool(  list_cpf )
        return free_or_block

    @staticmethod
    def verify_status_cpf_with_pandas(cpf: str) -> bool: 
        """[
            Função alternativa feita com pandas para verificar o status do cpf.
        ]
        Args:
            cpf (str): [String com 14 caracteres]
        Returns:
            bool: [Retorna True se o cpf estiver no arquivo e False se não estiver.]
        """
        df = pd.read_fwf('./blacklist.txt', names=["cpf"])
        free_or_block = cpf in df.values
        return free_or_block
   
    @staticmethod
    def format_cpf(cpf: str) -> str:
        """[Função responsável por formatar o cpf]

        Args:
            cpf (str): [String com 11 caracteres decimais.]

        Returns:
            str: [Retorna o cpf formatado.]
        """
        cpf_formated = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        return cpf_formated
    
    @staticmethod
    def remove_special_characters(cpf: str) -> str:
        """[
            Função responsável por remover caracteres especiais do cpf.
        ]

        Args:
            cpf (str): [String com 11 ou 14 caracteres.]

        Returns:
            str: [Retorna apenas caracteres númericos.]
        """
        numbers_cpf = filter(str.isdigit, cpf)
        numbers_cpf = "".join(numbers_cpf)
        return numbers_cpf