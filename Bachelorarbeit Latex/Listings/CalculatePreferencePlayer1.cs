public String calculatePreferencePlayer1() {
	String preference = "";
	if (isFirstTurn && freeBuild) {
		preference = "wood";
	} else if (isSecondTurn && freeBuild) {
		preference = "brick";
	} else if (isAbledToBuildCity) {
		preference = "";
	} else if (isAbledToBuildVillage) {
		if (wheat == 2 && stone == 2) {
			preference = "rock";
		} else if (stone == 3 && wheat == 1) {
			preference = "wheat";
		}
	} else {
		preference = "";
	}
	this.preference = preference;
	return preference;
}