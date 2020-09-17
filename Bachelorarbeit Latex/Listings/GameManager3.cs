   public void OnRollDice()
    {
        // left mouse button clicked so roll random colored dice 2 of each dieType
        Dice.Clear();
        Dice.Roll("1d6", "d6-" + "red", spawnPoint.transform.position, Force());
        Dice.Roll("1d6", "d6-" + "red", spawnPoint.transform.position, Force());
        rollDiceBtn.interactable = false;

        StartCoroutine(AddResources());
        StartCoroutine(EnableEndTurn());
    }

    private Vector3 Force()
    {
        Vector3 rollTarget = Vector3.zero + new Vector3(2 + 7 * Random.value, .5F + 4 * Random.value, -2 - 3 * Random.value);
        return Vector3.Lerp(spawnPoint.transform.position, rollTarget, 1).normalized * (-35 - Random.value * 20);
    }

    IEnumerator AddResources()
    {
        yield return new WaitForSeconds(3f);
        int number = Dice.GetValue("");
        player1.CollectResources(number);
        player2.CollectResources(number);
        activePlayer.UpdateResources();
    }

    IEnumerator EnableEndTurn()
    {
        yield return new WaitForSeconds(4f);
        endTurnBtn.interactable = true;
    }