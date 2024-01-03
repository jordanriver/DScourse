import nbformat
from nbconvert import PDFExporter
import os
from traitlets.config import Config
import uuid
from nbconvert import LatexExporter


def main():
    pass


def convert_ipynb_to_pdf(source_file_path, output_directory):
    # Ensure the source file exists
    if not os.path.isfile(source_file_path):
        print("File not found: ", source_file_path)
        return

    # Ensure the output directory exists, create if it doesn't
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Load the notebook
    with open(source_file_path, "r", encoding="utf-8") as file:
        nb = nbformat.read(file, as_version=4)

    # Add a unique identifier to each output file name
    for cell in nb.cells:
        if "outputs" in cell:
            for output in cell["outputs"]:
                if "filename" in output.get("metadata", {}):
                    unique_id = str(uuid.uuid4())
                    original_filename = output["metadata"]["filename"]
                    unique_filename = f"{unique_id}_{original_filename}"
                    output["metadata"]["filename"] = unique_filename

    # Convert to PDF
    pdf_exporter = PDFExporter()
    pdf_exporter.exclude_input = False

    # Export to PDF
    body, _ = pdf_exporter.from_notebook_node(nb)

    # Write to a PDF file in the specified output directory
    pdf_file_name = os.path.basename(source_file_path).replace(".ipynb", ".pdf")
    pdf_file_path = os.path.join(output_directory, pdf_file_name)

    with open(pdf_file_path, "wb") as file:
        file.write(body)
    print("Converted to PDF: ", pdf_file_path)


# Example usage
# convert_ipynb_to_pdf_with_unique_output('path_to_your_notebook.ipynb', 'your_output_directory')


def convert_ipynb_to_pdf_with_custom_title(
    source_file_path, output_directory, custom_title
):
    # Ensure the source file exists
    if not os.path.isfile(source_file_path):
        print("File not found: ", source_file_path)
        return

    # Ensure the output directory exists, create if it doesn't
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Load the notebook
    with open(source_file_path, "r", encoding="utf-8") as file:
        nb = nbformat.read(file, as_version=4)

    # Configure PDF Exporter with a custom title
    c = Config()
    c.PDFExporter.preprocessors = ["nbconvert.preprocessors.ExtractOutputPreprocessor"]
    c.PDFExporter.exclude_input = False
    c.PDFExporter.latex_elements = {
        "preamble": r"""
        \title{"""
        + custom_title
        + r"""}
        \author{}  % Remove the author field
        \date{}    % Remove the date field
        \usepackage{listings}
        \lstset{
            breaklines=true,
            breakatwhitespace=true,
            basicstyle=\small\ttfamily,
            frame=single,
            framesep=2pt,
            framerule=0pt,
            xleftmargin=2pt,
            xrightmargin=2pt,
            columns=fullflexible,
            keepspaces=true,
            escapeinside={(*@}{@*)},
        }
        \usepackage{geometry}
        \geometry{left=1cm,right=1cm,top=1cm,bottom=1cm}
        """
    }

    # Convert to PDF with customized settings
    pdf_exporter = PDFExporter(config=c)
    body, _ = pdf_exporter.from_notebook_node(nb)

    # Write to a PDF file in the specified output directory
    pdf_file_name = os.path.basename(source_file_path).replace(".ipynb", ".pdf")
    pdf_file_path = os.path.join(output_directory, pdf_file_name)

    with open(pdf_file_path, "wb") as file:
        file.write(body)
    print("Converted to PDF: ", pdf_file_path)


# Example usage
# convert_ipynb_to_pdf_with_custom_title('path_to_your_notebook.ipynb', 'your_output_directory', 'Your Custom Title')


def convert_ipynb_to_latex(source_file_path, output_directory):
    # Ensure the source file exists
    if not os.path.isfile(source_file_path):
        print("File not found: ", source_file_path)
        return

    # Ensure the output directory exists, create if it doesn't
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Load the notebook
    with open(source_file_path, "r", encoding="utf-8") as file:
        nb = nbformat.read(file, as_version=4)

    # Convert to LaTeX
    latex_exporter = LatexExporter()
    latex_exporter.exclude_input = False
    body, _ = latex_exporter.from_notebook_node(nb)

    # Write to a LaTeX file in the specified output directory
    latex_file_name = os.path.basename(source_file_path).replace(".ipynb", ".tex")
    latex_file_path = os.path.join(output_directory, latex_file_name)

    with open(latex_file_path, "w", encoding="utf-8") as file:
        file.write(body)
    print("Converted to LaTeX: ", latex_file_path)


# Example usage
# convert_ipynb_to_latex('path_to_your_notebook.ipynb', 'your_output_directory')


if __name__ == "__main__":
    main()
