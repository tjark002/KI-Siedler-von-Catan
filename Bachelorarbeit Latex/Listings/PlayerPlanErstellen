if (allowedToRollDice) {
	RollDice();
	first = true;
} else if (HasResourcesForCity() || HasResourcesForVillage() || HasResourcesForRoad()){
	if (HasResourcesForCity() && first && map.cityPlacesExist()) {
		triesCity++;
		first = false;
		ActivateCityPlaces();
	} else if (HasResourcesForCity() && !first && map.cityPlacesExist() && triesCity <= 3) {
		triesRoad = 0;
		triesCity = 0;
		triesVillage = 0;
		first = true;
		BuildCity(map.getRandomCityPlace());
		ActivateCityPlaces();
	} else if (HasResourcesForVillage() && (first || triesVillage == 0)) {
		triesVillage++;
		first = false; 
		ActivateVillagePlaces();
	} else if (HasResourcesForVillage() && !first && map.villagePlacesActive() && triesVillage <= 3) {
		triesRoad = 0;
		triesCity = 0;
		triesVillage = 0;
		first = true; 
		BuildVillage(map.getRandomVillagePlace());
		ActivateVillagePlaces();
	} else if (HasResourcesForRoad() && (first || triesRoad == 0)) {
		triesRoad++;
		first = false;
		ActivateRoadPlaces();
	} else if (HasResourcesForRoad() && !first && triesRoad <= 3) {
		triesRoad = 0;
		triesCity = 0;
		triesVillage = 0;
		first = true;
		BuildRoad(map.getRandomRoadPlace());
		ActivateRoadPlaces();
	}
} else {
	EndTurn();
}