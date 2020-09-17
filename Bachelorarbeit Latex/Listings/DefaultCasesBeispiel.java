//Konkreter Fall für den ersten Zug, wenn ein kostenloses Dorf gebaut werden darf
Status firstTurnVillage = new Status();

//Wichtig
firstTurnVillage.villagePlacesActive = true;
firstTurnVillage.isFirstTurn = true;
firstTurnVillage.isSecondTurn = false;
firstTurnVillage.freeBuild = true;
firstTurnVillage.freeBuildRoad = false;


//Unwichtig
firstTurnVillage.victoryPoints = 0;
firstTurnVillage.longestRoad = 0;
firstTurnVillage.hasLongestRoad = false;

firstTurnVillage.bricks = 0;
firstTurnVillage.wheat = 0;
firstTurnVillage.stone = 0;
firstTurnVillage.wood = 0;
firstTurnVillage.sheep= 0;

//firstTurnVillage.villages = new ArrayList<~>();
//firstTurnVillage.roads = new ArrayList<~>();

firstTurnVillage.isAbledToEndTurn = false;
firstTurnVillage.allowedToRollDice = false;

plan = "BuildVillage;ActivateVillagePlaces";
status.put(firstTurnVillage, plan);