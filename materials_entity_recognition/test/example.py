import os
import json
from pprint import pprint
from materials_entity_recognition import MatRecognition
from materials_entity_recognition import MatIdentification

__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the JSON file
    json_path = r"C:\Users\dilla\Downloads\text-mined-aunp-synthesis_public-main\text-mined-aunp-synthesis_public-main\aunp-synthesis_dataset_2021-9-14.json\aunp-synthesis_dataset_2021-9-14.json"

    # load data
    with open(json_path, 'r') as fr:
        paras = json.load(fr)

    # # find materials
    # model_new = MatIdentification()
    # for tmp_para in paras[-1:]:
    #     result = model_new.mat_identify(tmp_para)
    #     pprint(result)

    # find targets/precursors
    model_new = MatRecognition()
    # It would be much faster to input a list of paragraphs
    # rather than input them one by one in a loop !
    result = model_new.mat_recognize(paras)
    pprint(result)