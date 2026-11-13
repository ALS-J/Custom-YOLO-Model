Description: YOLO means "You only look once" which is a camera detection model for objects.This 
github repo is a YOLO code base, you can use it to make and train your own custom YOLO's easily

Rules:
1. Follow the instructions in order below to ensure it works as intended
2. Please follow the green '#' notes in the python code files
3. If you're going to use this publicly, please do give me credit and link my github

Instructions:
For making the custom labeling: (SKIP IF ALREADY EXPORTED THEM FROM LABEL-STUDIO)
    1. Take pictures of the objects you want to detect(Recommend: Pictures in the same lighting as  the ones when you use your pc camera) and put them in a folder
    2. In the command terminal, create python virtual environment in version 3.12, type 'py -3.12 -m venv CustomYOLO'
    3. Put all the python files in the virtual environment and then, in the command terminal, type 'CustomYOLO\Scripts\activate' (Excluding the '')
    4. In the command terminal again, type 'python -m pip install label-studio' after it's done, type 'python -m pip install ultralytics' and wait until it's done
    5. After step 4, type in the command terminal 'label-studio' should open up a localhost website in your browser
    5. In the label-studio website, signup/login
    6. Click on create project, make the name, description, and import the folder you put the pictures in
    7. Go to labeling setup, pick a template, and click add the new label names then save 
    8. Start labeling/Use tutorial on how to label using label-studio
    9. Once you submitted all the annotations, export them into a 'YOLO with images' format

After the custom labeling:
    1. Fill in the python code where there are green '#' notes with the directory/Info it is asking for
        (You get the directory through your file explorer and find them then go to the title where the directory is and copy)
    2. Read the green '#' notes clearly and listen to thme
    3. Once done, run then in this order: (Make sure the last file you ran is finished before moving to the next one) YOLOSplitData.py -> CustomYOLOTrain.py -> CustomYOLORun.py
    4. It should work. Thank you for using my repo.
