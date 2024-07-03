from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import os

# Defina os genes housekeeping que você deseja concatenar
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

# Diretório contendo os arquivos FASTA
fasta_files_dir = "./fasta_files/"

# Função para carregar sequências de cada gene
def load_sequences(gene):
    sequences = {}
    file_path = os.path.join(fasta_files_dir, f"{gene}_sequences.fasta")
    for record in SeqIO.parse(file_path, "fasta"):
        sequences[record.id] = record.seq
    return sequences

# Carregar todas as sequências para os genes definidos
all_sequences = {gene: load_sequences(gene) for gene in housekeeping_genes}

# Obter a lista de todas as linhagens presentes em pelo menos um gene
linhagens = set()
for sequences in all_sequences.values():
    linhagens.update(sequences.keys())
linhagens = sorted(linhagens)

# Verificar o número de linhagens únicas
if len(linhagens) != 15:
    print(f"Erro: número de linhagens únicas esperado é 15, mas foi encontrado {len(linhagens)}")
else:
    print("Número de linhagens está correto")

# Concatenar as sequências de cada linhagem com gaps onde necessário
concatenated_sequences = []
for linhagem in linhagens:
    concatenated_seq = ''
    for gene in housekeeping_genes:
        if linhagem in all_sequences[gene]:
            concatenated_seq += str(all_sequences[gene][linhagem])
        else:
            # Adicionar gaps do tamanho da sequência do gene ausente
            concatenated_seq += '-' * len(next(iter(all_sequences[gene].values())))
    # Criar um registro de sequência concatenada
    concatenated_record = SeqRecord(Seq(concatenated_seq), id=linhagem, description="")
    concatenated_sequences.append(concatenated_record)

# Salvar o alinhamento concatenado em um arquivo FASTA
output_file_path = os.path.join(fasta_files_dir, "concatenated_sequences_with_gaps.fasta")
with open(output_file_path, "w") as output_handle:
    SeqIO.write(concatenated_sequences, output_handle, "fasta")

print(f"Sequências concatenadas com gaps e salvas em {output_file_path}.")
