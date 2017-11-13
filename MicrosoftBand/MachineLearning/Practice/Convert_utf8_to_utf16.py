import codecs
import shutil

with codecs.open("/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/test.csv", encoding="utf-8") as input_file:
    with codecs.open(
            "/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/test_converted.csv", "w", encoding="utf-16") as output_file:
        shutil.copyfileobj(input_file, output_file)