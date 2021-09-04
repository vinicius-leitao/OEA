#include <string.h>
#include <iostream>

typedef struct _Endereco Endereco;

//Professor, tive que ficar atento ao meu arquivo .dat pois o primeiro registro começa em 1, logo fiquei um bom tempo pra descobrir que tava pegando um elemento anterior ao do meio para testar, hahahaha. Só pra deixar registrado caso aconteça com o sr. Valeu!

struct _Endereco
{
    char logradouro[72];
    char bairro[72];
    char cidade[72];
    char uf[72];
    char sigla[2];
    char cep[8];
    char lixo[2];
};

int main(int argc, char **argv)
{
    FILE *f;
    Endereco e;

    int passos;
    long inicio, meio, fim, tamArq, tamReg, x;

    if (argc != 2)
    {
        fprintf(stderr, "USO: %s [CEP]", argv[0]);
        return 1;
    }

    //Abre o arquivo
    f = fopen("cep_ordenado.dat", "r");

    //Seta o inicio para 0
    inicio = 0;

    //Descobre o tamanho do Arquivo
    fseek(f, 0, SEEK_END);
    tamArq = ftell(f);
    rewind(f);

    //Guarda o tamanho do registro
    tamReg = sizeof(Endereco);

    //Seta o fim
    fim = (tamArq / tamReg) - 1;

    //Inicializa passos
    passos = 0;
    while (inicio <= fim)
    {
        passos++;
        meio = (inicio + fim) / 2;

        //Posiciona o ponteiro no registro do meio.
        fseek(f, meio * tamReg, SEEK_CUR);
        // Lê o registro
        fread(&e, tamReg, 1, f);

        //Comparações e atualizações de variaveis fim e inicio.
        if (strncmp(argv[1], e.cep, 8) == 0)
        {
            printf("%.72s\n%.72s\n%.72s\n%.72s\n%.2s\n%.8s\n", e.logradouro, e.bairro, e.cidade, e.uf, e.sigla, e.cep);
            break;
        }
        else if (strncmp(argv[1], e.cep, 8) < 0)
        {
            fim = meio - 1;
        }
        else if (strncmp(argv[1], e.cep, 8) > 0)
        {
            inicio = meio + 1;
        }

        //Volta ao inicio do arquivo.
        rewind(f);
    }

    std::cout << "Achei com " << passos << " passos!" << std::endl;
    fclose(f);

    return 0;
}