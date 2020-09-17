	if (roadFocus.hasFocus && (activePlayer.HasResourcesForRoad() || activePlayer.isFirstTurn || activePlayer.isSecondTurn))
    {
        roadPlaces.SetActive(true);
        foreach (GameObject village in activePlayer.villages)
        {
            Transform transform = roadPlaces.GetComponent<Transform>();
            for (int i = roadPlaces.GetComponent<Transform>().childCount - 1; i >= 0; i--)
            {
                Transform child = transform.GetChild(i);
                float distance = (village.transform.position - child.position).magnitude;
                if (distance < roadRange)
                {
                    child.gameObject.SetActive(true);
                }
            }
        }
        foreach (GameObject road in activePlayer.roads)
        {
            Transform transform = roadPlaces.GetComponent<Transform>();
            for (int i = roadPlaces.GetComponent<Transform>().childCount - 1; i >= 0; i--)
            {
                Transform child = transform.GetChild(i);
                float distance = (road.transform.position - child.position).magnitude;
                if (distance < roadRange)
                {
                    child.gameObject.SetActive(true);
                }
            }
        }

        if (buildRoad != null)
        {
            if (!activePlayer.freeBuild && !activePlayer.freeBuildRoad && (activePlayer.isFirstTurn || activePlayer.isSecondTurn))
                endTurnBtn.interactable = true;
        }
    } else
    {
        ... //Deaktivieren wie für die Siedlungen
    }
}