import subprocess
import sys

def convert_docx_to_md(input_file, output_file):
    """
    Converte um arquivo .docx para .md usando Pandoc.
    """
    try:
        subprocess.run([
            "pandoc",
            input_file,
            "-f", "docx",
            "-t", "markdown",
            "-o", output_file
        ], check=True)
        print(f"Arquivo convertido: {output_file}")
    except FileNotFoundError:
        print("Erro: Pandoc não está instalado ou não está no PATH.")
    except subprocess.CalledProcessError:
        print("Erro ao converter o arquivo.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python html-or-docx-for-md.py <entrada.docx> <saida.md>")
    else:
        convert_docx_to_md(sys.argv[1], sys.argv[2])