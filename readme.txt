Project: Visualsation of Pi
By: Aman Goyal

Vriable Terminology:

1,2 : Heavy Box, Lighter box
s: side
x,y : coordinated
m: mass
v: velocity
step : used to increase smoothness of animaion
let_collision: used to create the collision effect

power: maintaining ratio of mass of blocks in order of 100**x

Known Problems:
#Animation Glitch On left wall for high mass ratios(power)>=4->Solved
Sound not playing well for high mass ratios(power)>=3

KnownSolutions:
#Animation Glitch: Added pseudo animation for smaller block when both blocks are colliding fast.