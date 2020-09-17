/**
 * Die Buttons muesssen zuerst deaktiviert werden, sonst kann dies von den KIs ausgenutzt werden
 */
private void Awake()
{
    endTurnBtn.interactable = false;
    rollDiceBtn.interactable = false;
}


/**
 * Start wird nach Awake aufgerufen und setzt die Namen der Spieler, sowie einige Variablen und bestimmt wer den ersten Zug hat. 
 */
void Start()
{
    player1.isAI = PlayerPrefs.GetInt("player1Ai") == 1 ? true : false;
    player2.isAI = PlayerPrefs.GetInt("player2Ai") == 1 ? true : false;
    player1.name = "Player1";
    player1.SetGameManager(this);
    player2.name = "Player2";
    player2.SetGameManager(this);
    UpdateActivePlayer(player1);

    if (isSpeedUp) {
        enableEndTurnWait = 0.1f;
        addResourcesWait = 0.05f; 
        MakeAiTurnWait = 0.4f; 
        MakeAiMainTurnWait = 0.5f;
    } else
    {
        enableEndTurnWait = 4f;
        addResourcesWait = 3f;
        MakeAiTurnWait = 4f;
        MakeAiMainTurnWait = 5f;
    }

    lateStart = true;
}