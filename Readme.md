

# Concatenar Genes Housekeeping

Este projeto contém um script Python desenvolvido para concatenar sequências de genes housekeeping a partir de arquivos FASTA. O script carrega sequências de genes específicos, identifica linhagens presentes em cada gene, e concatena as sequências, adicionando gaps onde necessário. O resultado é um arquivo FASTA contendo as sequências concatenadas para cada linhagem, pronto para análises subsequentes.

## Requisitos

- Python 3.x
- Biopython

## Instalação

1. Clone este repositório:

   git clone https://github.com/BiazzMoura/Concatenando_sequencias.git 
   cd Concatenando_sequencias

2. Instale as dependências necessárias:

   pip install biopython

## Uso

1. Coloque seus arquivos FASTA no diretório especificado no script (`fasta_files_dir`). Certifique-se de que os arquivos tenham a extensão `.fna`.

2. Defina os genes housekeeping que você deseja concatenar no script. Por exemplo:
   
   housekeeping_genes = [
       "ddrA",
       "ddrB",
       "GAP",
       "gyrA",
       "polA",
       "recA",
       "ruvB",
       "uvrD"
   ]

3. Execute o script:

   python concatenate.py

4. O script lerá todos os arquivos `.fna` no diretório especificado, identificará as sequências dos genes housekeeping, concatenará as sequências e salvará o resultado em um arquivo FASTA.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões, sinta-se à vontade para abrir uma issue ou enviar um pull request.

