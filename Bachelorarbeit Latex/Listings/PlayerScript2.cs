 //Sorgt für die richtigen Einstellungen zu Beginn eines Zuges
    public void FirstTurn()
    {
        AdjustCamera();
        isFirstTurn = true;
        freeBuild = true;
        freeBuildRoad = false;
    }

    public void SecondTurn()
    {
        AdjustCamera();
        isFirstTurn = false;
        isSecondTurn = true;
        freeBuild = true;
        freeBuildRoad = false;
    }

    public void Turn()
    {
        AdjustCamera();
        freeBuild = false;
        freeBuildRoad = false;
        isFirstTurn = false;
        isSecondTurn = false;
    }

    private void AdjustCamera()
    {
        cameraView.transform.position = playerView;
    }