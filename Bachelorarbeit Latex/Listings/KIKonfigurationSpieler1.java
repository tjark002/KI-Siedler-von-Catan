public void updateAttributeWeight(Status status) {
	
	if (status.isFirstTurn || status.isSecondTurn) {
		isFirstTurn = 1000;
		hasFreeBuild = 900;
		hasFreeBuildRoad = 900;
		villagePlacesAct = 800;
		roadPlacesAct = 800;
		
	} else if (status.isSecondTurn) {
		isSecondTurn = 1000;
		hasFreeBuild = 900;
		hasFreeBuildRoad = 900;
		villagePlacesAct = 800;
		roadPlacesAct = 800;
		
	} else if(status.allowedToRollDice) {
		
		isAllowedToRollDice = 1000;
		
	} else if(!status.allowedToRollDice) { 
		
		if (status.hasResourcesForCity()) {
			if (!status.cityPlacesActive) {
				isAbledToBuildCity = 100;
				cityPlacesAct = 1000;
				isAbledToBuildVillage = 100;
				isAbledToBuildRoad = 100;
				isAbledToEndTurn = 100;
				
			} else if (status.cityPlacesActive) {
				isAbledToBuildCity = 1000;
				cityPlacesAct = 100;
				isAbledToBuildVillage = 100;
				isAbledToBuildRoad = 100;
				isAbledToEndTurn = 100;
			}

		} else if (status.hasResourcesForVillage()) {
			if (!status.villagePlacesActive) {
				isAbledToBuildVillage = 100;
				villagePlacesAct = 1000;
				isAbledToBuildVillage = 100;
				isAbledToBuildRoad = 100;
				isAbledToEndTurn = 100;
				
			} else if (status.villagePlacesActive) {
				isAbledToBuildVillage = 1000;
				villagePlacesAct = 100;
				isAbledToBuildVillage = 100;
				isAbledToBuildRoad = 100;
				isAbledToEndTurn = 100;
			}

		} else if (status.hasResourcesForRoad ()) {
			if (!status.roadPlacesActive) {
				isAbledToBuildRoad = 100;
				roadPlacesAct = 1000;
				isAbledToBuildVillage = 100;
				isAbledToBuildRoad = 100;
				isAbledToEndTurn = 100;
				
			} else if (status.roadPlacesActive) {
				isAbledToBuildRoad = 1000;
				roadPlacesAct = 100;
				isAbledToBuildVillage = 100;
				isAbledToBuildRoad = 100;
				isAbledToEndTurn = 100;
			}
			
		} else {
			isAbledToEndTurn = 1000;
			isAbledToBuildRoad = 100;
			roadPlacesAct = 100;
			isAbledToBuildVillage = 100;
			isAbledToBuildRoad = 100;
			isAbledToBuildVillage = 100;
			villagePlacesAct = 100;
			isAbledToBuildCity = 100;
			cityPlacesAct = 100;
		} 
	}
}