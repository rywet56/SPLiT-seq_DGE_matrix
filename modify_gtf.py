# def get_gtf_content(gtf_in_path):
#     # the output:
#     # [[['1', 'araport11', 'gene', '3631', '5899', '.', '+', '.'], {'gene_id': 'AT1G01010', 'gene_name': 'NAC001', 'gene_source': 'araport11', 'gene_biotype': 'protein_coding'}], [['1', 'araport11', 'transcript', '3631', '5899', '.', '+', '.'], {'gene_id': 'AT1G01010', 'transcript_id': 'AT1G01010.1', 'gene_name': 'NAC001', 'gene_source': 'araport11', 'gene_biotype': 'protein_coding', 'transcript_source': 'araport11', 'transcript_biotype': 'protein_coding'}], [['1', 'araport11', 'exon', '3631', '3913', '.', '+', '.'], {'gene_id': 'AT1G01010', 'transcript_id': 'AT1G01010.1', 'exon_number': '1', 'gene_name': 'NAC001', 'gene_source': 'araport11', 'gene_biotype': 'protein_coding', 'transcript_source': 'araport11', 'transcript_biotype': 'protein_coding', 'exon_id': 'AT1G01010.1.exon1'}], [['1', 'araport11', 'CDS', '3760', '3913', '.', '+', '0'], {'gene_id': 'AT1G01010', 'transcript_id': 'AT1G01010.1', 'exon_number': '1', 'gene_name': 'NAC001', 'gene_source': 'araport11', 'gene_biotype': 'protein_coding', 'transcript_source': 'araport11', 'transcript_biotype': 'protein_coding', 'protein_id': 'AT1G01010.1'}], [['1', 'araport11', 'start_codon', '3760', '3762', '.', '+', '0'], {'gene_id': 'AT1G01010', 'transcript_id': 'AT1G01010.1', 'exon_number': '1', 'gene_name': 'NAC001', 'gene_source': 'araport11', 'gene_biotype': 'protein_coding', 'transcript_source': 'araport11', 'transcript_biotype': 'protein_coding'}]]
#
#     handler = open(gtf_in_path)
#     gtf_content = handler.readlines()
#
#     gtf_lines = [""] * len(gtf_content)
#     i = 0
#     for read in gtf_content:
#         first = read.split("\t")[0:8]  # --> ['1', 'araport11', 'gene', '3631', '5899', '.', '+
#
#         second = read.split("\t")[8].split(";")[:-1]
#
#         second_dic = {}
#         for pair in second:
#             split_pair = pair.strip().replace('"', "").split(' ')
#             print(split_pair)
#             second_dic[split_pair[0]] = split_pair[1]
#
#         gtf_lines[i] = [first, second_dic]
#         i += 1
#
#     return gtf_lines


def get_gtf_content(gtf_in_path):
    # the output:
    # [[['1', 'araport11', 'gene', '3631', '5899', '.', '+', '.'], {'gene_id': 'AT1G01010', 'gene_name': 'NAC001', 'gene_source': 'araport11', 'gene_biotype': 'protein_coding'}], [['1', 'araport11', 'transcript', '3631', '5899', '.', '+', '.'], {'gene_id': 'AT1G01010', 'transcript_id': 'AT1G01010.1', 'gene_name': 'NAC001', 'gene_source': 'araport11', 'gene_biotype': 'protein_coding', 'transcript_source': 'araport11', 'transcript_biotype': 'protein_coding'}], [['1', 'araport11', 'exon', '3631', '3913', '.', '+', '.'], {'gene_id': 'AT1G01010', 'transcript_id': 'AT1G01010.1', 'exon_number': '1', 'gene_name': 'NAC001', 'gene_source': 'araport11', 'gene_biotype': 'protein_coding', 'transcript_source': 'araport11', 'transcript_biotype': 'protein_coding', 'exon_id': 'AT1G01010.1.exon1'}], [['1', 'araport11', 'CDS', '3760', '3913', '.', '+', '0'], {'gene_id': 'AT1G01010', 'transcript_id': 'AT1G01010.1', 'exon_number': '1', 'gene_name': 'NAC001', 'gene_source': 'araport11', 'gene_biotype': 'protein_coding', 'transcript_source': 'araport11', 'transcript_biotype': 'protein_coding', 'protein_id': 'AT1G01010.1'}], [['1', 'araport11', 'start_codon', '3760', '3762', '.', '+', '0'], {'gene_id': 'AT1G01010', 'transcript_id': 'AT1G01010.1', 'exon_number': '1', 'gene_name': 'NAC001', 'gene_source': 'araport11', 'gene_biotype': 'protein_coding', 'transcript_source': 'araport11', 'transcript_biotype': 'protein_coding'}]]

    handler = open(gtf_in_path)
    gtf_content = handler.readlines()

    gtf_lines = [""] * len(gtf_content)
    i = 0
    for read in gtf_content:
        first = read.split("\t")[0:8]  # --> ['1', 'araport11', 'gene', '3631', '5899', '.', '+

        second = read.split("\t")[8].split('";')[:-1]
        second_dic = {}
        for pair in second:
            split_pair = pair.strip().replace('"', "").split(' ')
            second_dic[split_pair[0]] = split_pair[1]

        gtf_lines[i] = [first, second_dic]
        i += 1

    return gtf_lines


def write_gtf_content(gtf_out_path, gtf_content):
    handler = open(gtf_out_path, 'w')

    for line in gtf_content:
        handler.write(line[0][0] + "\t" + line[0][1] + "\t" + line[0][2] + "\t" + line[0][3] + "\t" + line[0][4] +
                      "\t" + line[0][5] + "\t" + line[0][6] + "\t" + line[0][7] + "\t")
        round = 0
        for tag in line[1].items():
            if round != 0:  # only make a space starting with the second round
                handler.write(" ")
            handler.write(tag[0] + " " + '"' + tag[1] + '"' + ";")
            round += 1
        handler.write("\n")


def get_tag_value(gtf_line, tag_name):
    return gtf_line[1][tag_name]


def add_tag(gtf_line, tag_name, tag_value):
    gtf_line[1][tag_name] = tag_value


def is_tag(gtf_line, tag_name):
    return tag_name in gtf_line[1]


# read in content of .gtf file
gtf_content = get_gtf_content("/Users/manuel/Downloads/gtf_modification/Arabidopsis_thaliana.TAIR10.46.gtf")

# for every line in the gtf file that has a tag "transcript_id" add a tag "transcript_name" that has the value of
# "transcript_id"

for line in gtf_content:
    if is_tag(line, "transcript_id"):
        tag_value = get_tag_value(line, "transcript_id")
        add_tag(line, "transcript_name", tag_value)
    if is_tag(line, "gene_id"):
        tag_value = get_tag_value(line, "gene_id")
        add_tag(line, "gene_name", tag_value)

# write content to harddrive as .gtf file
write_gtf_content("/Users/manuel/Downloads/gtf_modification/AT_modified_2.gtf", gtf_content)
