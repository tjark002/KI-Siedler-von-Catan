...
void ChangePlayer()
{
    cameraView.transform.Rotate(0.0f, 180.0f, 0.0f, 0);
    if (activePlayer == player1)
    {
        UpdateActivePlayer(player2);
    }
    else
    {
        UpdateActivePlayer(player1);
    }
    activePlayer.Turn();
}

private void UpdateActivePlayer(PlayerScript player)
{
    activePlayer = player;

    activePlayer.UpdateVictoryPoints();
    if (player1.longestRoad > player2.longestRoad)
    {
        player1.victoryPoints += 2;
    } else if (player1.longestRoad < player2.longestRoad)
    {
        player2.victoryPoints += 2;
    }
	
	... //Aktivierung der Bauplätze

    buildVillage[] buildVillages = villagePlaces.GetComponentsInChildren<buildVillage>();
    foreach (buildVillage build in buildVillages)
    {
        build.player = activePlayer;
    }

    ... //Deaktivierung der Bauplätze

    ... //Aktivierung der Bauplätze

    BuildRoad[] buildRoads = roadPlaces.GetComponentsInChildren<BuildRoad>();
    foreach (BuildRoad build in buildRoads)
    {
        build.player = activePlayer;
    }

    ... //Deaktivierung der Bauplätze
}