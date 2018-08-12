# AbsolueFaces
A demo Facial recognition 
1.Methodology Used:
LBPH(Local Binary Pattern Histrogram)-> labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number. 
In simple terms if this is an window of 3x3
[8  7   6]                                                                  [1  1   1]
[4  5   9]--->taking N neighbours of 5 we have thus 5 being the Theshold -->[0      1]
[1  7   3]                                                                  [0   1  0]
-->11101010 the thus value of 5 is now deci(11101010)

so all the pixels are converted in this manner
then the image is converted into grids and thus converted into a histrogram

New images that come in are then converted in same manner and are compared with the saved model

2.Resources you used for it:
python 3.5x
openCV3.3
pyCharm IDE
Numpy

3.Step by step guide to reproduce the results:
        1. create 2 directory : FILE and dataset
                                FILE will have 'fface.xml' or frontal face cascade xml file
                                dataset empty for now
        2.Run dataSetCreator.py file
              a)first Have to give some input id -->any integer
              b)after that keep your face infront of the web cam and it will click pictures of you and save in dataset directory
        3.Run trainer.py file
              this will create a YML file in the FILE directory
        4. Run Recognizer.py file
              this will give you the facial Recognition with Your id num
      
 
