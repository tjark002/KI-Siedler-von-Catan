public void updateAttributeWeight(Status status) {
	
	if (status.isFirstTurn) {
		isFirstTurn = 1000;
		isSecondTurn = 0;
		hasFreeBuild = 900;
		hasFreeBuildRoad = 900;
		villagePlacesAct = 800;
		roadPlacesAct = 800;
		
	} else if (status.isSecondTurn) {
		... //Äquivalent zu isFirstTurn
	} else if(status.allowedToRollDice) {
		
		isAllowedToRollDice = 1000;
		
	} else if(!status.allowedToRollDice) { 
		
		flush();
		if (status.hasResourcesForCity()) {
			if (!status.getMap().cityPlacesActive()) {
				isAbledToBuildCity = 100;
				cityPlacesAct = 1000;
				
			} else if (status.getMap().cityPlacesActive()) {
				isAbledToBuildCity = 1000;
			}

		} else if (status.hasResourcesForVillage()) {
			if (!status.getMap().villagePlacesActive()) {
				isAbledToBuildVillage = 100;
				villagePlacesAct = 1000;
				
			} else if (status.getMap().villagePlacesActive()) {
				isAbledToBuildVillage = 1000;
			}

		} else if (status.hasResourcesForRoad()) {
			if (!status.getMap().roadPlacesActive()) {
				isAbledToBuildRoad = 100;
				roadPlacesAct = 1000;
				
			} else if (status.getMap().roadPlacesActive()) {
				isAbledToBuildRoad = 1000;
				roadPlacesAct = 100;
			}
			
		} else {
			isAbledToEndTurn = 1000;
			... //Restliche auf 0 setzen
		} 
	}
}