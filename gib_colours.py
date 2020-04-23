# -*- coding: utf-8 -*-
import poppler
import sys
import urllib
import os

def which_colours(input_path):

    document = poppler.document_new_from_file('file://%s' % \
    urllib.pathname2url(os.path.abspath(input_path)), None)
    n_pages = document.get_n_pages()
    all_annots = 0

    unique_colours = []

    for i in range(n_pages):
        page = document.get_page(i)
        annot_mappings = page.get_annot_mapping()
        #print("## annot mappings ##")
        #print(annot_mappings)
        num_annots = len(annot_mappings)
        if num_annots > 0:
            for annot_mapping in annot_mappings:
                if  annot_mapping.annot.get_annot_type().value_name != 'POPPLER_ANNOT_LINK':
                    #print annot_mapping.annot.get_color()
                    all_annots += 1
                    rgb = []
                    try:
                        rgb.append(annot_mapping.annot.get_color().red)
                        rgb.append(annot_mapping.annot.get_color().green)
                        rgb.append(annot_mapping.annot.get_color().blue)
                    except AttributeError:
                        pass
                        continue

                    if rgb not in unique_colours:
                        unique_colours.append(rgb)

    print("Unique colours: ", unique_colours)


if __name__ == '__main__':
    which_colours(sys.argv[1])
