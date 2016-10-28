import csv
from fpdf import *


class MyFPDF(FPDF, HTMLMixin):
    pass


def output_csv(matrix):
    try:
        with open('matrix.csv', 'w') as csvfile:
            fieldnames = range(0, len(matrix) + 1)
            writer = csv.DictWriter(csvfile, lineterminator='\n', delimiter=';', fieldnames=fieldnames)
            writer.writeheader()

            for i, line in enumerate(matrix):
                temp_line = {0: i + 1}
                for j, value in enumerate(line):
                    temp_line[j + 1] = value.__round__(2)
                writer.writerow(temp_line)
    except IOError:
        print('ERROR: The CSV file could not be created, permission denied. Check if the file does not already exists and is not currently opened.')
    else:
        print('A CSV file has been created in the root project folder.')


def matrix_to_html(matrix):
    pourcent_width = int(100 / (len(matrix) + 1))
    str_pourcent_width = str(pourcent_width) + '%'
    html = '<table><thead><tr><th width="'+str_pourcent_width+'">&nbsp;</th>'
    for i in range(1, len(matrix) + 1):
        html += '<th width="'+str_pourcent_width+'">Page ' + str(i) + '</th>'
    html += '</tr></thead><tbody>'

    for i, line in enumerate(matrix):
        html += '<tr><td align="center"><b>Page ' + str(i + 1) + '</b></td>'
        for j, value in enumerate(line):
            html += '<td align="center">' + str(value) + '</td>'
        html += '</tr>'
    html += '</tbody></table>'
    return html


def infos_to_html(infos):
    str = ''
    for info in infos:
        str += '<div>' + info + '</div><br />'
    return str


def output_html(matrix, infos, shingle_size):
    pdf = MyFPDF()
    pdf.add_page()

    with open('output_template.html', 'r') as myfile:
        html = myfile.read()
    html = html.replace('[MATRIX]', matrix_to_html(matrix))
    html = html.replace('[INFOS]', infos_to_html(infos))
    html = html.replace('[SHINGLES]', str(shingle_size))

    pdf.write_html(html)

    try:
        pdf.output('matrix.pdf', 'F')
    except IOError:
        print('ERROR: The PDF file could not be created, permission denied. Check if the file does not already exists and is not currently opened.')
    else:
        print('A PDF file has been created in the root project folder.')
