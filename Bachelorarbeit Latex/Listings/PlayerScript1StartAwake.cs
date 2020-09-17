    private void Awake()
    {
        isFirstTurn = false;
        isSecondTurn = false;
        longestRoad = 0;
        victoryPoints = 0;
        roadRange = 1.1f;
    }

    void Start()
    {
        brickTxt.text = "Lehm: " + brick.ToString();
        woodTxt.text = "Holz: " + wood.ToString();
        wheatTxt.text = "Getreide: " + wheat.ToString();
        sheepTxt.text = "Schafe: " + sheep.ToString();
        stoneTxt.text = "Stein: " + stone.ToString();

        villages = new List<GameObject>();
    }