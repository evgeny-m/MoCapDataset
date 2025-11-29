# MoCapDataset
Motion capture dataset obtained using the Perception Neuron system

This repository contains a motion capture dataset obtained using a perception neuron system for classifying human actions.

The dataset is divided into several parts: gestures, controls, and tool use.

## Part 1 - Gestures
This part contains the following gestures:
1. Thumb up
2. Thumb down
3. Show closed index finger and thumb ("OK")
4. Wave goodbye
5. Rock open palm with back up ("so-so")
6. Show extended thumb and pinky ("call me")
7. Show index finger up ("quiet")
8. Show index and middle fingers up (victory "V" sign)
9. Beckon with index finger
10. Wag with index finger

## Part 2 - Control
This part contains the following gestures:
1. Double palm movement toward you ("start moving toward me")
2. Double palm movement away from you ("start moving away from me")
3. Double palm movement to the left ("move/turn left relative to me")
4. Double palm movement to the right ("move/turn right relative to me")
5. Single vertical wave of an open palm ("stop")
6. Repeated circular motion of the raised index finger ("start")
7. Carrying an imaginary object with the index and thumb fingers ("carrying a bag with fingers gesture")
8. Single palm movement to the left ("scroll left")
9. Single palm movement to the right ("scroll right")
10. Single palm movement down ("scroll down")
11. Single palm movement up ("scroll up")
12. Forward hand movement with opening thumb and index finger ("zoom in")
13. Backward hand movement with narrowing of thumb and index finger ("zoom out")
14. Double forward hand movement with clockwise wrist rotation
15. Double backward hand movement with counterclockwise wrist rotation
16. Single forward hand movement with clockwise wrist rotation ("add value")
17. Single backward hand movement with counterclockwise wrist rotation ("decrease value")
18. Upward hand movement with clenched fist ("close")

## Part 3 - Using Tools
This section contains actions performed with the following tools:
1. Hammer a nail
2. Tighten a screw with a screwdriver
3. Loosen a screw with a screwdriver
4. Tighten with a ring spanner (box wrench)
5. Loosen with a ring spanner (box wrench)
6. Tighten with a hex key
7. Loosen with a hex key
8. Install a clamp
9. Remove a clamp
10. Stapler
11. Cut with a hacksaw (option 1)
12. Cut with a hacksaw (option 2)
13. Sharpen with a file
14. Paint with a brush
15. Cut with scissors
16. Stir with a spoon

## Methodology
Before recording, the actors were instructed to perform the actions consistently. 
Before recording, the actors had the opportunity to repeat the actions without the suit one or more times. Before performing the actions, 
the actors' experience with the tools varied, sometimes even to the point of complete inexperience.

The first and second parts of the set were recorded on the same day. 
The third part was recorded on a different day and time. We tried to include consistently performed actions from all classes within a single part in a single recording. 
We recorded each part for each actor five times. Thus, each action class was represented by 20 instances. After each recording, we recalibrated the capture system.

The recorded sequences were carefully segmented manually to separate the actions of different classes over time. 
The sequences were exported from the motion capture software as processed .bvh files. 
Each movement instance was then converted into a separate sequence of frames containing 3D coordinated and saved as a .pkl file. 
Each .pkl file therefore contains contains one example of some  motion class performed by one of the actors as a sequence of frames, 
where each frame represents a sequence of 3D coordinates of individual body parts.

## File Naming

Each file in the data set has a name in the following format: <br>
<i>\<part\>AA_II_CC.pkl</i><br>
where <i>\<part\></i> is the name of the data set part ("gest" - gestures, "ctrl" - control, "inst" - tool handling),<br>
<i>AA</i> is the actor number,<br>
<i>AI</i> is the instance number,<br>
<i>CC</i> is the movement class number.

The dataset should contain: 4 x 5 x 10 = 200 files in the first part, 4 x 5 x 18 = 360 files in the second part, and 4 x 5 x 16 = 320 files in the third part. 
Unfortunately, some isolated sequences were excluded from the dataset. Therefore, the dataset in the current version contains 876 files.
