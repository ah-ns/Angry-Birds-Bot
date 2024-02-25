<h2>Angry Birds bot</h2>

Make computer vision to spot pigs on the map
(since the pigs' models vary quite a bit, it is easier to detect using color matching)

TODO:
--
Simulate mouse movement to be able to shoot the birds

Determine trajectory based on distance of mouse from slingshot and angle <br>
Maybe take the distance between the slingshot and the lowest pig and determine the angle and scale at which to pull the slingshot. (if there is noticable pattern) <br>
++++++++<br>
Use a vector as the constant movement from the launch added to the gravity vector - the launch vector will be a conbination of the horizontal velocity and the upward velocity, the gravity vector will be a downward accelerating one <br>
++++++++<br>
Then, get points based on the vectors and create a polynomial, solving for the position a pig is close to

Determine when to use a power (Ex. when to explode the bomb guy) - maybe figure out how fast the birds travel and click based on how far away the structure is

Determine which bird to use based on the material of the structure



FIX:
--
Prevent errors if there are no find results (find_by_image and find_by_color functions)

