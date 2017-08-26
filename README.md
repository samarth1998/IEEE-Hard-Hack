# IEEE-Hard-Hack
Hardware Hackathon at UC San Diego conducted by Qualcomm and IEEE

This is a project that my team developed during H.A.R.D Hack at UC San Diego.

We tried to make a face recognition personal wardrobe for a family of 5 people. The idea was that in the future people will love to save space in the house and would love to have a single closet.
We have used a webcam to detect motion (through Microsoft API's). Whenever there is a motion, the camera makes sure that the person gets his/her face in the center of the camera. The user is informed about the right position through a beep. Once the face is in the right position, the camera then captures a .png file.
The .png file is then transferred to an online cloud where we have already stored different images of all the family members. Once the algorithm recognizes the correct person, the arduino displays the name of the family user on a LCD display and rotates the wardrobe useing a motor. 

For this project we used
- 2 Arduino UNO
- LCD Display
- Proximity Sensor
- webcam
- A desktop screen (to monitor activity)
- Wifi Module 
- Mictrosoft API

We couldn't finish the motor part (the revolving wardrobe phase) due to time constraints.
