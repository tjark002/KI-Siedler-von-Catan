public String calculatePreferencePlayer2() {
	String preference = "";
	if (isFirstTurn && freeBuild) {
		preference = "wood";
	} else if (isSecondTurn && freeBuild) {
		preference = "brick";
	} else if (isAbledToBuildCity) {
		preference = "";
	} else if (isAbledToBuildVillage) {
		if (bricks < wood || bricks == wood) {
			if (bricks < sheep || bricks == sheep) {
				if (bricks < wheat || bricks == wheat) {
					preference = "brick";
				} else {
					if (wheat < sheep || wheat == sheep) {
						preference = "wheat";
					} else {
						preference = "sheep";
					}
				}
			} else {
				if (sheep < wheat) {
					preference = "sheep";
				} else {
					preference = "wheat";
				}
			}
		} else {
			if (wood < sheep || wood == sheep) {
				preference = "wood";
			} else {
				if (wheat < sheep || wheat == sheep) {
					preference = "wheat";
				} else {
					preference = "sheep";
				}
			}
		}
	} else {
		preference = "";
	}
	this.preference = preference;
	return preference;
}