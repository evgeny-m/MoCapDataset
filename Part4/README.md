## File format
Each .pkl file stores a pair (<i>xs, ys</i>), 
where <i>xs</i> is the pose sequences and <i>ys</i> is the motion classes. 
</br>
As each .pkl file in the current version of the dataset contains information about a single motion sequence 
both <i>xs</i> and <i>ys</i> contain one element each. 
The motion class is also contained in the file name, so it can be ignored.
</br>
The pose sequence from <i>xs</i> is a list of poses. The length of the list can vary.
</br></br>
Each pose in a sequence is described by a set of joint positions</br> 
[<i> J<sub>1,1</sub>, J<sub>1,2</sub>, J<sub>1,3</sub>, J<sub>2,1</sub>, J<sub>2,2</sub>, J<sub>2,3</sub>, 
J<sub>3,1</sub>, J<sub>3,2</sub>, J<sub>3,3</sub>, ... </i>]. </br>
The joints follow one another in a specific order, with the three spatial coordinates of the first joint specified first, 
then the three coordinates of the second, and so on. 
The set of joints depends on the dataset part and does not change. 
Thus, the pose space dimension remains constant within a single dataset part.
## Joints
Part 4 uses the following joint sequence:
- Hips,
- RightUpLeg,
- RightLeg,
- RightFoot,
- LeftUpLeg,
- LeftLeg,
- LeftFoot,
- Spine,
- Spine1,
- Spine2,
- Spine3,
- Neck,
- Head,
- RightShoulder,
- RightArm,
- RightForeArm,
- RightHand,
- RightHandThumb1,
- RightHandThumb2,
- RightHandThumb3,
- RightInHandIndex,
- RightHandIndex1,
- RightHandIndex2,
- RightHandIndex3,
- RightInHandMiddle,
- RightHandMiddle1,
- RightHandMiddle2,
- RightHandMiddle3,
- RightInHandRing,
- RightHandRing1,
- RightHandRing2,
- RightHandRing3,
- RightInHandPinky,
- RightHandPinky1,
- RightHandPinky2,
- RightHandPinky3,
- LeftShoulder,
- LeftArm,
- LeftForeArm,
- LeftHand,
- LeftHandThumb1,
- LeftHandThumb2,
- LeftHandThumb3,
- LeftInHandIndex,
- LeftHandIndex1,
- LeftHandIndex2,
- LeftHandIndex3,
- LeftInHandMiddle,
- LeftHandMiddle1,
- LeftHandMiddle2,
- LeftHandMiddle3,
- LeftInHandRing,
- LeftHandRing1,
- LeftHandRing2,
- LeftHandRing3,
- LeftInHandPinky,
- LeftHandPinky1,
- LeftHandPinky2,
- LeftHandPinky3.
	
