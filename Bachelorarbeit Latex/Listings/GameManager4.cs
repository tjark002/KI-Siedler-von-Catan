    public void OnEndTurn()
    {
        if (activePlayer.victoryPoints > 3)
        {

        }
        if (activePlayer.isFirstTurn && activePlayer == player1)
        {
            UpdateActivePlayer(player2);
            cameraView.transform.Rotate(0.0f, 180.0f, 0.0f, 0);

            activePlayer.FirstTurn();
            endTurnBtn.interactable = false;
            rollDiceBtn.interactable = false;
        }
        else if (activePlayer.isFirstTurn && activePlayer == player2)
        {
            activePlayer.SecondTurn();
            endTurnBtn.interactable = false;
            rollDiceBtn.interactable = false;
        }
        else if (activePlayer.isSecondTurn && activePlayer == player2)
        {
            activePlayer.CollectResourcesForVillage
				(activePlayer.villages[activePlayer.villages.Count - 1]);
            UpdateActivePlayer(player1);
            cameraView.transform.Rotate(0.0f, 180.0f, 0.0f, 0);

            activePlayer.SecondTurn();
            endTurnBtn.interactable = false;
            rollDiceBtn.interactable = false;
        }
        else if (activePlayer.isSecondTurn && activePlayer == player1)
        {
            activePlayer.CollectResourcesForVillage
				(activePlayer.villages[activePlayer.villages.Count - 1]);
            activePlayer.Turn();
            endTurnBtn.interactable = false;
            rollDiceBtn.interactable = true;
        }
        else
        {
            ChangePlayer();
            rollDiceBtn.interactable = true;
            endTurnBtn.interactable = false;
        }
        activePlayer.UpdateResources();
    }