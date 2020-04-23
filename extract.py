# -*- coding: utf-8 -*-

import poppler
import sys
import urllib
import os
import re
from settings import *


def hl2md(input_path, md_folder):
    input_split = input_path.rsplit('/', 1)[-1]
    print(input_split)

    # removes ".pdf" from filename
    filename_base = input_split[:-4]
    print("Input use 4: ", filename_base)

    output_filename = md_folder+filename_base+'_hl.md'

    bib = '@'+filename_base

    document = poppler.document_new_from_file('file://%s' % \
    urllib.pathname2url(os.path.abspath(input_path)), None)
    n_pages = document.get_n_pages()
    all_annots = 0

    outer_output = []

    for i in range(n_pages):
        page = document.get_page(i)
        annot_mappings = page.get_annot_mapping()

        num_annots = len(annot_mappings)
        if num_annots > 0:
            for annot_mapping in annot_mappings:
                if  annot_mapping.annot.get_annot_type().value_name != 'POPPLER_ANNOT_LINK':
                    all_annots += 1
                    rgb = []
                    try:
                        rgb.append(annot_mapping.annot.get_color().red)
                        rgb.append(annot_mapping.annot.get_color().green)
                        rgb.append(annot_mapping.annot.get_color().blue)
                    except AttributeError:
                        pass
                        continue

                    contents = str(annot_mapping.annot.get_contents()).replace('\n', ' ').replace('\r', '')
                    contents = re.sub("\s\s+" , " ", contents)
                    contents = re.sub("\t", " ", contents)

                    try:
                        md_cite = '"'+contents+'" ['+bib+': '+str(i+1)+']'
                    except Exception as e:
                        md_cite = ''


                    for col in colours:
                        for code in col['codes']:
                            if rgb == code['rgb-hex']:
                                print("Match")
                                category = col['category']

                    try:
                        output = 'page: {0:3} \nbib: {1} \n{2:10} \ncategory: {3}  \ncontent: {4} \npandoc_cite: {5}'.format(i+1, bib, annot_mapping.annot.get_modified(), category, contents, md_cite)
                    except Exception as e:
                        output = 'page: {0:3} \nbib: {1} \n{2:10} \ncategory: {3}  \ncontent: {4} \npandoc_cite: {5}'.format(i+1, bib, annot_mapping.annot.get_modified(), 'hors-categorie', contents, md_cite)

                    outer_output.append(output)


    if not os.path.exists(md_folder):
        os.makedirs(md_folder)

    with open(output_filename, 'w+') as f:
        f.writelines('[text]'+'\n'+'bib: '+bib+'\n\n'+'[.Highlight]'+'\n\n')

        for i in outer_output:
            f.write(i+'\n\n')

        f.writelines('[]')

    if all_annots > 0:
        print str(all_annots) + " annotation(s) found"
    else:
        print "no annotations found"

    return output_filename
