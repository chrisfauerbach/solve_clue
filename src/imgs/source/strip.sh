#!/bin/bash
let START_X=15
let X=15
let Y=15
let WIDTH=98
let HEIGHT=150
let MOVE_Y=154
let MOVE_X=98
echo "convert rose: -crop 40x30+10+10  crop.gif"
echo "convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  white.jpg"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../white.jpg
let "X = $X + $MOVE_X"
echo "convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  peacock.jpg"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../peacock.jpg
let "X = $X + $MOVE_X"
echo "convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../scarlett.jpg"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../scarlett.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../mustard.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../green.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../plum.jpg
let "X = $START_X"
let "Y = $Y + $MOVE_Y"
echo "convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../candlestick.jpg"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../candlestick.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../revolver.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../rope.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../wrench.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../leadpipe.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../knife.jpg
let "X =  $START_X"
let "Y = $Y + $MOVE_Y"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../study.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../library.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../convervatory.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../hall.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../kitchen.jpg
let "X = $START_X"
let "Y = $Y + $MOVE_Y"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../ballroom.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../diningroom.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../lounge.jpg
let "X = $X + $MOVE_X"
convert master.jpg -crop ${WIDTH}x${HEIGHT}+$X+$Y  ../billiardroom.jpg
