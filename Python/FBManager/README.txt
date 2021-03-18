Simple football manager "game" implemented only to practise Python programming.

User first choose his team and then continue selecting 1st or 2nd squad to play. 
AI generates results using certain rules and probabilities, and then updates a league table. By default there 
are six teams and they play two times against each other. Team names and couple other values are configurable 
in params.py. 

Team squads doesn't have actual players. They only have a one value to represent a whole squad skill level. 
Squads also have a fit level which decreases if a squad is chosen to play and recovers when a squad rests.